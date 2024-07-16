<a href="https://huggingface.co/spaces/neonwatty/bleep_that_sht" target="_parent"><img src="https://img.shields.io/badge/🤗-HuggingFace%20Space-cyan.svg" alt="HuggingFace Space"/></a>
<a href="https://colab.research.google.com/github/jermwatt/bleep_that_sht/blob/main/beep_that_sht_walkthrough.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  <a href="https://www.youtube.com/watch?v=U8Ki9dD3HF0" target="_parent"><img src="https://badges.aleen42.com/src/youtube.svg" alt="Youtube"/></a>
[![Python application](https://github.com/neonwatty/bleep_that_sht/actions/workflows/python-app.yml/badge.svg)](https://github.com/neonwatty/bleep_that_sht/actions/workflows/python-app.yml/python-app.yml) <a href="https://www.producthunt.com/posts/bleep-that-sh-t?embed=true&utm_source=badge-featured&utm_medium=badge&utm_souce=badge-bleep&#0045;that&#0045;sh&#0045;t" target="_parent"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=470378&theme=light" alt="Bleep&#0032;That&#0032;Sh&#0042;t&#0033; - A&#0032;whisper&#0032;app&#0032;that&#0032;bleeps&#0032;out&#0032;chosen&#0032;words&#0032;in&#0032;YouTube&#0032;videos | Product Hunt" style="width: 300px; height: 45px;" /></a>


# bleep that sh*t

Make anyone sound naughty / funny with Python.

Bleep out keywords of your choice from an mp4 by leveraging a transcription model (here Whisper) to transcribe the audio, then target and replace chosen words with *bleep* sounds using the extracted timestamps associated with your chosen word(s).  

All processing is performed locally - see the streamlit app (setup below) and detailed walkthrough notebook (see `beep_that_sht_walkthrough.ipynb`) to play / see nitty gritty details.  Click [![HuggingFace Space](https://img.shields.io/badge/🤗-HuggingFace%20Space-cyan.svg)](https://huggingface.co/spaces/neonwatty/bleep_that_sht) to try out this toy app directly in your browser.  WARNING: the machine this Space is running on is pretty small - so use it to try out shorter (<2min) videos.

Some examples of the end product (make sure to turn volume on, its off by default).

https://github.com/user-attachments/assets/da50f8a9-27ba-4747-92e0-72a25e65175c

Let's look more closely at the last example above - below is a short clip we'll bleep out some words from using the pipeline in this repo.  (make sure to turn on audio - its off by default)

https://github.com/neonwatty/bleep_that_sht/assets/16326421/fb8568fe-aba0-49e2-a563-642d658c0651


Now the same clip with the words - "treetz", "ice", "cream", "chocolate", "syrup", and "cookie" - bleeped out


https://github.com/neonwatty/bleep_that_sht/assets/16326421/63ebd7a0-46f6-4efd-80ea-20512ff427c0


## Install instructions

To get setup to run the notebook / bleep your own videos / run the strealit demo first install the requirements for this project by pasting the below in your terminal.

```python
pip install -r requirements.txt
```

You will need [ffmpeg](https://www.ffmpeg.org/download.html) installed on your machine as well.



## Instructions for bleeping **youtube** videos via youtube / shorts url

Start this streamlit demo locally that lets you enter in a youtube / shorts url to a video you wish to bleep

```python
python -m streamlit run bleep_that_sht/app_url_download.py
```

Alternatively you can start a gradio server with the same functionality

```python
python -m bleep_that_sht/gradio_app_url_download.py
```

This is the version hosted in the HF space [![HuggingFace Space](https://img.shields.io/badge/🤗-HuggingFace%20Space-cyan.svg)](https://huggingface.co/spaces/neonwatty/bleep_that_sht).



## Instructions for bleeping your own **local** videos

Start this streamlit demo locally that lets you drag and drop local video files to bleep

```python
python -m streamlit run bleep_that_sht/app_video_upload.py
```