#!/command/with-contenv bash
# with-contenv exposes SUPERVISOR_TOKEN; exec keeps the container stdin for hassio.app_stdin.
set -euo pipefail
cd /opt/htbw_voice_evidence
exec /opt/venv/bin/python -m htbw_voice_evidence
