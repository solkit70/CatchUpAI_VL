---
marp: true
theme: gaia
class: invert
paginate: true
lang: ko
style: |
  :root {
    --color-foreground: #e8f0fe;
    --color-background: #1a2744;
    --color-highlight: #22C55E;
  }
  section {
    background-color: #1d3a6e;
    background-image:
      radial-gradient(ellipse at 5% 5%, rgba(34,197,94,0.18) 0%, transparent 45%),
      radial-gradient(ellipse at 95% 95%, rgba(56,189,248,0.14) 0%, transparent 45%),
      radial-gradient(ellipse at 90% 5%, rgba(245,158,11,0.10) 0%, transparent 35%),
      radial-gradient(circle at 1.5px 1.5px, rgba(255,255,255,0.06) 1.5px, transparent 0);
    background-size: 100% 100%, 100% 100%, 100% 100%, 32px 32px;
    color: #e8f0fe;
    font-family: 'Noto Sans KR', 'Malgun Gothic', sans-serif;
  }
  h1 {
    color: #22C55E;
    font-size: 1.6em;
    border-bottom: 2px solid rgba(34,197,94,0.35);
    padding-bottom: 0.15em;
    margin-bottom: 0.4em;
  }
  h2 {
    color: #F59E0B;
    font-size: 1.3em;
    letter-spacing: -0.01em;
  }
  h3 { color: #60A5FA; }
  strong { color: #F59E0B; }
  a { color: #60A5FA; }
  blockquote {
    border-left: 4px solid #22C55E;
    background: rgba(34, 197, 94, 0.10);
    padding: 0.5em 1em;
    font-size: 0.95em;
    color: #bbf7d0;
    border-radius: 0 8px 8px 0;
    margin: 0.6em 0;
  }
  table {
    font-size: 0.82em;
    width: 100%;
    border-collapse: collapse;
  }
  th {
    background: rgba(34,197,94,0.22);
    color: #22C55E;
    padding: 6px 10px;
  }
  td { padding: 5px 10px; }
  tr:nth-child(even) { background: rgba(255,255,255,0.06); }
  tr:nth-child(odd) { background: rgba(255,255,255,0.02); }
  code {
    background: rgba(34,197,94,0.14);
    color: #a7f3d0;
    padding: 0.15em 0.4em;
    border-radius: 4px;
    font-size: 0.88em;
  }
  pre {
    background: rgba(10,16,38,0.75);
    border: 1px solid rgba(34,197,94,0.3);
    border-radius: 10px;
    padding: 0.8em 1em;
    font-size: 0.82em;
  }
  pre code { background: transparent; color: #a7f3d0; padding: 0; }
  .lead h1 { font-size: 2em; text-align: center; }
  section.title { padding-top: 40px; padding-bottom: 30px; }
  section.title h1 { font-size: 1.55em; margin-bottom: 0.1em; }
  section.title h2 { font-size: 0.95em; text-align: center; margin-bottom: 0.35em; }
  section.title p { font-size: 0.75em; margin-top: 0.3em; }
  .title-row { display: flex; align-items: flex-end; justify-content: center; gap: 28px; margin: 0.2em auto 0; }
  .title-thumb img { width: 400px; border-radius: 10px; border: 2px solid rgba(34,197,94,0.5); box-shadow: 0 4px 20px rgba(0,0,0,0.35); display: block; }
  .title-qr img { width: 132px; border-radius: 8px; background: #fff; padding: 4px; display: block; margin: 0 auto; }
  .title-row .cap { font-size: 0.55em; color: #bbf7d0; text-align: center; margin-top: 6px; line-height: 1.3; max-width: 400px; }
  .lead p { text-align: center; font-size: 1.1em; }
  section.lead {
    background-image:
      radial-gradient(ellipse at 50% 35%, rgba(34,197,94,0.25) 0%, transparent 60%),
      radial-gradient(ellipse at 5% 100%, rgba(56,189,248,0.18) 0%, transparent 50%),
      radial-gradient(circle at 1.5px 1.5px, rgba(255,255,255,0.06) 1.5px, transparent 0);
    background-size: 100% 100%, 100% 100%, 32px 32px;
  }
  video {
    width: 100%;
    max-height: 38vh;
    border-radius: 10px;
    border: 2px solid rgba(34,197,94,0.5);
    box-shadow: 0 4px 20px rgba(34,197,94,0.18);
    margin-bottom: 0.6em;
  }
  .clip-label {
    font-size: 0.75em;
    color: #64748b;
    text-align: right;
    margin-top: 4px;
  }
---
