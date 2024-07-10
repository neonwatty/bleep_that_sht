[![HuggingFace Space](https://img.shields.io/badge/🤗-HuggingFace%20Space-cyan.svg)](https://huggingface.co/spaces/neonwatty/bleep_that_sht)
<a href="https://colab.research.google.com/github/jermwatt/bleep_that_sht/blob/main/beep_that_sht_walkthrough.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  <a href="https://www.youtube.com/watch?v=U8Ki9dD3HF0" target="_parent"><img src="https://badges.aleen42.com/src/youtube.svg" alt="Youtube"/></a>


# bleep that sh*t

Make anyone sound naughty with Python.

Bleep out keywords of your choice from an mp4 by leveraging a transcription model (here Whisper) to transcribe the audio, then target and replace chosen words with *bleep* sounds using the extracted timestamps associated with your chosen word(s).  

All processing is performed locally - see the streamlit app (setup below) and detailed walkthrough notebook (see `beep_that_sht_walkthrough.ipynb`) to play / see nitty gritty details.  Click [![HuggingFace Space](https://img.shields.io/badge/🤗-HuggingFace%20Space-cyan.svg)](https://huggingface.co/spaces/neonwatty/bleep_that_sht) to try out this toy app directly in your browser.  WARNING: the machine this Space is running on is pretty small - so use it to try out shorter (<2min) videos.

An example - below is a short clip we'll bleep out some words from using the pipeline in this repo.  (make sure to turn on audio - its off by default)


https://github.com/neonwatty/bleep_that_sht/assets/16326421/fb8568fe-aba0-49e2-a563-642d658c0651


Now the same clip with the words - "treetz", "ice", "cream", "chocolate", "syrup", and "cookie" - bleeped out


https://github.com/neonwatty/bleep_that_sht/assets/16326421/63ebd7a0-46f6-4efd-80ea-20512ff427c0



## Install instructions

To get setup to run the notebook / bleep your own videos / run the strealit demo first install the requirements for this project by pasting the below in your terminal.

```python
pip install -r requirements.txt
```

You will need [ffmpeg](https://www.ffmpeg.org/download.html) installed on your machine as well.


## Instructions for bleeping your own **local** videos

Start this streamlit demo locally that lets you drag and drop local video files to bleep

```python
python -m streamlit run bleep_that_sht/app_video_upload.py
```

## Instructions for bleeping **youtube** videos via youtube / shorts url

Start this streamlit demo locally that lets you enter in a youtube / shorts url to a video you wish to bleep

```python
python -m streamlit run bleep_that_sht/app_url_download.py
```

This is the version hosted in the HF space [![HuggingFace Space](https://img.shields.io/badge/🤗-HuggingFace%20Space-cyan.svg)](https://huggingface.co/spaces/neonwatty/bleep_that_sht).
