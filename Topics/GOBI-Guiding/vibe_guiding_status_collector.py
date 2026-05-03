import os
import sys
import platform
import yaml
import json
import subprocess

def get_system_status():
    """시스템 및 앱 환경 정보를 수집하여 반환합니다."""
    status = {
        "os": {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version()
        },
        "tools": {
            "python": sys.version.split()[0],
            "node": None,
            "gobi_cli": None
        },
        "gobi_settings": {}
    }

    # Node.js 버전 확인
    try:
        node_ver = subprocess.check_output(["node", "--version"], text=True).strip()
        status["tools"]["node"] = node_ver
    except:
        pass

    # Gobi CLI 버전 확인
    try:
        gobi_ver = subprocess.check_output(["npx", "@gobi-ai/cli", "--version"], text=True).strip()
        status["tools"]["gobi_cli"] = gobi_ver
    except:
        pass

    # .gobi/settings.yaml 파일 읽기
    settings_path = ".gobi/settings.yaml"
    if os.path.exists(settings_path):
        try:
            with open(settings_path, 'r', encoding='utf-8') as f:
                settings = yaml.safe_load(f)
                status["gobi_settings"] = settings
        except Exception as e:
            status["gobi_settings"] = {"error": str(e)}

    return status

if __name__ == "__main__":
    current_status = get_system_status()

    # 결과를 예쁘게 JSON으로 출력
    print(json.dumps(current_status, indent=2, ensure_ascii=False))

    # 로컬 파일로 저장하여 에이전트가 참조하도록 함
    save_path = "Ingest/CatchUpAI_VL/Topics/GOBI-Guiding/current_system_context.json"
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, 'w', encoding='utf-8') as f:
        json.dump(current_status, f, indent=2, ensure_ascii=False)

    print(f"\n✅ 컨텍스트 수집 완료! 파일 저장됨: {save_path}")
