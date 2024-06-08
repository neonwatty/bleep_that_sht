# bleep that sh*t

This repo illustrates how to use a transcription model to automatically bleep out desired words from an input video.

It contains a streamlit demo (see below) and detailed walkthrough notebook.

## Install instructions

To get setup to run the notebook / bleep your own videos / run the strealit demo first install the requirements for this project by pasting the below in your terminal.

```python
pip install -r requirements.txt
```


## Instructions for bleeping your own videos

Start the streamlit demo

```python
python -m streamlit run bleep_that_sht/app.py
```

You will see printouts at the terminal indicating success of the two smallest whisper model downloads - `tiny` and `base`.

Then you can drag and drop your own mp4 (note: only mp4 is accepted) videos into the demo app, define your own bleep_words, and process.

You can download your bleeped video by clicking on the three dots at the bottom right of the bleeped video, and clicking download.