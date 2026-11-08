# Debian (glibc) base: onnxruntime publishes no musl wheels, so Alpine cannot be used.
# Official Home Assistant Debian base image, pinned to a release tag.
FROM ghcr.io/home-assistant/base-debian:trixie-2026.11.0

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:${PATH}"

# Debian trixie python3 (3.13) in an isolated virtual environment.
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 python3-venv \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir --only-binary=:all: -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY htbw_voice_evidence /opt/htbw_voice_evidence/htbw_voice_evidence
COPY MODEL_LICENSE.md /opt/htbw_voice_evidence/MODEL_LICENSE.md
COPY rootfs /
RUN chmod 0755 /run.sh

WORKDIR /opt/htbw_voice_evidence
CMD ["/run.sh"]
