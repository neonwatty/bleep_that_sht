# Build stage
FROM python:3.10-slim AS builder

RUN apt-get update && \
    apt-get install -y \
    ffmpeg \
    build-essential \
    curl \
    software-properties-common && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /home

COPY requirements.gradio .

RUN pip3 install --no-cache-dir -r requirements.gradio

# Runtime stage
FROM python:3.10-slim

ENV PYTHONPATH=.

WORKDIR /home

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY bleep_that_sht /home/bleep_that_sht

EXPOSE 8501

ENTRYPOINT ["python", "/home/bleep_that_sht/gradio_app_url_download.py", "--server-port 8501", "--server-name 0.0.0.0"]