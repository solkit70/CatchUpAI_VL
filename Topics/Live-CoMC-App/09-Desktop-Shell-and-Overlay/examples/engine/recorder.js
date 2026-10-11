// Independent MediaRecorder files retain WebM headers (Catch's online-listening pattern).
let recording = null, recordBusy = false, voice = null;
const recError = message => { $('record-error').textContent = message || ''; };
const recMime = () => MediaRecorder.isTypeSupported('audio/webm;codecs=opus') ? 'audio/webm;codecs=opus' : 'audio/webm';

async function refreshMicDevices() {
  let temporary;
  try {
    temporary=await navigator.mediaDevices.getUserMedia({audio:true});
    const selected=$('rec-device').value;
    const devices=await navigator.mediaDevices.enumerateDevices();
    const inputs=devices.filter(d=>d.kind==='audioinput');
    $('rec-device').replaceChildren(new Option('기본 마이크', ''));
    for(const [i,d] of inputs.entries()) $('rec-device').add(new Option(d.label||`마이크 ${i+1}`,d.deviceId));
    if(inputs.some(d=>d.deviceId===selected))$('rec-device').value=selected;
    else {
      const active=temporary.getAudioTracks()[0]?.getSettings().deviceId;
      if(active && inputs.some(d=>d.deviceId===active))$('rec-device').value=active;
    }
    $('record-transcript-status').textContent=`입력 장치 ${inputs.length}개 확인 · 선택: ${$('rec-device').selectedOptions[0]?.textContent||'기본 마이크'}`;
  } catch(e) { recError('마이크 장치 확인 실패 · '+e.message); }
  finally { if(temporary) temporary.getTracks().forEach(t=>t.stop()); }
}

async function apiAudio(url, blob, id) {
  const response = await fetch(url, {method:'POST', body:blob, headers:id?{'X-Recording-Id':id}:{}});
  const result = await response.json();
  if(!response.ok || !result.ok) throw new Error(result.error || '음성을 처리하지 못했어요');
  return result;
}
function meterNode(ctx, stream, destination) {
  const source=ctx.createMediaStreamSource(stream), analyser=ctx.createAnalyser();
  analyser.fftSize=512;source.connect(analyser);if(destination)source.connect(destination);
  return analyser;
}
function volume(analyser) {
  if(!analyser)return 0;
  const xs=new Float32Array(analyser.fftSize);analyser.getFloatTimeDomainData(xs);
  const rms=Math.sqrt(xs.reduce((s,x)=>s+x*x,0)/xs.length);
  return Math.min(1,rms*10);
}
async function releaseAudio(c) {
  clearInterval(c.meterTimer);clearTimeout(c.timer);
  for(const stream of [c.mic,c.display,c.stream])if(stream)for(const track of stream.getTracks())track.stop();
  if(c.ctx)await c.ctx.close();
  $('mic-meter').value=$('remote-meter').value=0;
}
async function toggleRecording() {
  if(recordBusy)return;
  if(recording)return stopRecording();
  if(voice){recError('말로 요청을 마친 뒤 함께 듣기를 시작해 주세요.');return;}
  recordBusy=true;recError('');$('record-transcript-status').textContent='음성을 기다리고 있습니다.';$('record').disabled=true;
  const c={active:false,queue:Promise.resolve(),queued:0,id:null,rec:null,timer:null};
  try {
    if(!window.MediaRecorder)throw new Error('Chrome 또는 Edge에서 열어 주세요.');
    if($('rec-source').value==='mixed') {
      c.display=await navigator.mediaDevices.getDisplayMedia({video:true,audio:true});
      if(!c.display.getAudioTracks().length)throw new Error('공유할 때 탭/시스템 오디오도 선택해 주세요.');
    }
    const deviceId=$('rec-device').value;
    const audio={echoCancellation:false,noiseSuppression:false,autoGainControl:false};
    if(deviceId)audio.deviceId={exact:deviceId};
    c.mic=await navigator.mediaDevices.getUserMedia({audio});
    const track=c.mic.getAudioTracks()[0];
    $('record-transcript-status').textContent=`마이크 입력 중 · ${track.label||'선택한 장치'} · ${track.getSettings().sampleRate||'기본'} Hz`;
    c.ctx=new AudioContext();await c.ctx.resume();
    const mix=c.ctx.createMediaStreamDestination();c.stream=mix.stream;
    c.micMeter=meterNode(c.ctx,c.mic,mix);
    if(c.display)c.remoteMeter=meterNode(c.ctx,new MediaStream(c.display.getAudioTracks()),mix);
    const result=await post('/api/record/start');if(!result.ok)throw new Error(result.error);
    c.id=result.id;c.active=true;recording=c;
    c.sliceSpeechMs=0;
    c.meterTimer=setInterval(()=>{const level=volume(c.micMeter);$('mic-meter').value=level;$('remote-meter').value=volume(c.remoteMeter);if(level>=0.05)c.sliceSpeechMs+=100;},100);
    for(const stream of [c.mic,c.display])if(stream)for(const t of stream.getTracks())t.addEventListener('ended',()=>{if(recording===c)stopRecording();});
    $('record').textContent='⏹ 함께 듣기 멈춤';$('listen-card').classList.add('recording');
    nextSlice(c);
  } catch(e) {
    recError('함께 듣기 시작 실패 · '+e.message);
    if(c.id)await post('/api/record/stop',{id:c.id}).catch(()=>{});
    await releaseAudio(c);recording=null;
  } finally {recordBusy=false;$('record').disabled=false;}
}
function nextSlice(c) {
  if(!c.active || recording!==c)return;
  const chunks=[], rec=new MediaRecorder(c.stream,{mimeType:recMime(),audioBitsPerSecond:64000});c.rec=rec;
  rec.ondataavailable=e=>{if(e.data.size)chunks.push(e.data);};
  rec.onstop=()=>{
    c.rec=null;
    if(chunks.length) {
      const blob=new Blob(chunks,{type:'audio/webm'});
      if(c.sliceSpeechMs<500) {
        $('record-transcript-status').textContent='말소리가 감지되지 않아 조용한 구간은 전사하지 않았습니다.';
      } else if(blob.size>=2000) {
        c.queued++;
        c.queue=c.queue.then(()=>apiAudio('/api/record/audio',blob,c.id)).then(r=>{
          if(r.text){
            $('record-transcript-status').textContent=r.usable_for_assessment
              ? '최근 전사 · '+r.text
              : '불명확한 전사 1건을 화면 표시와 진행 평가에서 제외했습니다.';
          } else if(r.reason) {
            $('record-transcript-status').textContent='전사되지 않음 · '+r.reason;
          }
        }).catch(e=>{recError(e.message);}).finally(()=>{c.queued--;});
      }
    }
    c.sliceSpeechMs=0;
    if(c.queued>6){recError('받아 적기가 지연되어 녹음을 멈춥니다. 대기 음성을 저장한 뒤 다시 시작해 주세요.');stopRecording();return;}
    if(c.active)nextSlice(c);
  };
  rec.onerror=()=>{recError('녹음기 오류 · 입력을 확인한 뒤 다시 시작해 주세요.');stopRecording();};
  rec.start();c.timer=setTimeout(()=>{if(rec.state!=='inactive')rec.stop();},10000);
}
async function stopRecording() {
  if(recordBusy || !recording)return;
  recordBusy=true;$('record').disabled=true;
  const c=recording;c.active=false;clearTimeout(c.timer);
  try {
    if(c.rec&&c.rec.state!=='inactive')await new Promise(resolve=>{c.rec.addEventListener('stop',resolve,{once:true});c.rec.stop();});
    $('record-status').textContent='마지막 음성까지 저장·전사하고 있습니다…';
    await c.queue;
    const result=await post('/api/record/stop',{id:c.id});if(!result.ok)throw new Error(result.error);
    await post('/api/record/assess');
  } catch(e){recError('녹음 종료 확인 실패 · '+e.message);}
  finally {
    await releaseAudio(c);recording=null;recordBusy=false;
    $('record').textContent='⏺ 함께 듣기 시작';$('record').disabled=false;$('listen-card').classList.remove('recording');
  }
}
window.renderRecording=(r,playing)=>{
  if(!r)return;
  if(!recordBusy)$('record-status').textContent=(r.on?'⏺ 함께 듣는 중':'⏹ 함께 듣기 대기')+' · 받아 적기 '+r.count+'개 · 원본 음성 '+r.audio_segments+'개'+(r.checking?' · 진행 평가 중':'')+(r.on&&!r.count?' · 첫 음성을 기다리고 있어요':'');
  if(r.error)recError(r.error);
  const heardText=(r.lines||[]).map(x=>new Date(x.at).toLocaleTimeString()+' · '+
    (x.usable_for_assessment===false?'⚠ 불명확한 전사 (화면 표시·평가 제외)':x.text)).join('\n');
  if($('heard').textContent!==heardText){$('heard').textContent=heardText;$('heard').scrollTop=$('heard').scrollHeight;}
  const d=r.assessment;const box=$('assessment');const evidenceWasOpen=!!box.querySelector('details')?.open;box.replaceChildren();
  if(!d){box.textContent='실제로 들은 기록이 쌓이면 현재 이야기와 진행 상황을 표시합니다.';return;}
  for(const [label,value] of [['현재 이야기',d.topic],['확인된 완료',d.done.join(' / ')||'완료 확인 없음'],['남은 계획·확인할 일',d.remaining.join(' / ')||'미확인'],['코엠씨 제안',d.suggestion]]) {
    const p=document.createElement('p');p.style.margin='6px 0';const b=document.createElement('b');b.textContent=label+' · ';p.append(b,document.createTextNode(value||''));box.append(p);
  }
  const evidence=document.createElement('details'), title=document.createElement('summary');evidence.open=evidenceWasOpen;title.textContent='들은 근거 · '+new Date(d.at).toLocaleTimeString();evidence.append(title);
  const text=document.createElement('div');text.className='meta';text.textContent=d.evidence.map(e=>new Date(e.at).toLocaleTimeString()+' · '+e.quote).join(' / ');evidence.append(text);box.append(evidence);
};

async function toggleVoice() {
  if(recordBusy)return;
  if(voice){if(voice.rec.state!=='inactive')voice.rec.stop();return;}
  if(recording){recError('함께 듣기를 멈춘 뒤 말로 요청해 주세요. 방송 중에는 질문란에 입력할 수 있어요.');return;}
  try {
    const deviceId=$('rec-device').value;
    const audio={echoCancellation:false,noiseSuppression:false,autoGainControl:false};
    if(deviceId)audio.deviceId={exact:deviceId};
    const stream=await navigator.mediaDevices.getUserMedia({audio}), chunks=[];
    const ctx=new AudioContext();await ctx.resume();
    const analyser=meterNode(ctx,stream);
    const rec=new MediaRecorder(stream,{mimeType:recMime()});
    const activeVoice={rec,stream,ctx,analyser,meterTimer:null};
    voice=activeVoice;
    const track=stream.getAudioTracks()[0];
    $('record-transcript-status').textContent=`말로 요청 녹음 중 · ${track.label||'선택한 마이크'}`;
    activeVoice.meterTimer=setInterval(()=>{$('mic-meter').value=volume(analyser);},100);
    $('ptt').textContent='⏹ 요청 말하기 완료';
    rec.ondataavailable=e=>{if(e.data.size)chunks.push(e.data);};
    rec.onstop=async()=>{
      clearInterval(activeVoice.meterTimer);
      stream.getTracks().forEach(t=>t.stop());
      await ctx.close().catch(()=>{});
      $('mic-meter').value=0;
      if(voice===activeVoice)voice=null;
      $('record-transcript-status').textContent='말로 요청 음성을 전사하고 있습니다.';
      $('ptt').disabled=true;
      try {
        const r=await apiAudio('/api/stt',new Blob(chunks,{type:'audio/webm'}));
        if(r.text){$('q').value=r.text;await ask();}
        else $('question-message').textContent='말씀을 확인하지 못했어요. 다시 요청해 주세요.';
      }catch(e){$('question-message').textContent=e.message;}
      finally{$('record-transcript-status').textContent='';$('ptt').textContent='🎤 말로 요청';$('ptt').disabled=false;}
    };
    rec.start();setTimeout(()=>{if(rec.state!=='inactive')rec.stop();},30000);
  } catch(e){
    if(voice){clearInterval(voice.meterTimer);for(const track of voice.stream.getTracks())track.stop();await voice.ctx.close().catch(()=>{});voice=null;}
    $('mic-meter').value=0;
    recError('음성 입력 실패 · '+e.message);
  }
}
window.addEventListener('pagehide',()=>{if(recording)navigator.sendBeacon('/api/record/stop',new Blob([JSON.stringify({id:recording.id})],{type:'application/json'}));});
