FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN python3 --version && pip3 --version
RUN ffmpeg -version
    
ENV PYTHONPATH=.
ENV GRADIO_SERVER_PORT 8501
ENV GRADIO_SERVER_NAME "0.0.0.0"

WORKDIR /home

COPY requirements.gradio .

RUN pip3 install --no-cache-dir -r requirements.gradio
COPY bleep_that_sht /home/bleep_that_sht

ENTRYPOINT ["python3", "/home/bleep_that_sht/gradio_app_url_download.py"]