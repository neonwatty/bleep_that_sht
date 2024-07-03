<a href="https://colab.research.google.com/github/jermwatt/bleep_that_sht/blob/main/beep_that_sht_walkthrough.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# bleep that sh*t

Make someone sound naughty.

Bleep out keywords of your choice from an mp4 by leveraging a transcription model (here Whisper) to transcribe the audio, then target and replace chosen words with *bleep* sounds using the extracted timestamps associated with your chosen word(s.  

All processing is performed locally - see the streamlit app (setup below) and detailed walkthrough notebook (see `beep_that_sht_walkthrough.ipynb`) to play / see nitty gritty details.

An example - below is a short clip.  We can bleep out any word(s) we want - like "treats", "ice cream", "chocolate".

https://github.com/neonwatty/bleep_that_sht/assets/16326421/690032c5-6a42-442a-b208-fac6c6bd8458

Now the auto-bleeped version:

https://github.com/neonwatty/bleep_that_sht/assets/16326421/725a4b86-0a04-49ea-a2cf-df9d7657d79d


## Install instructions

To get setup to run the notebook / bleep your own videos / run the strealit demo first install the requirements for this project by pasting the below in your terminal.

```python
pip install -r requirements.txt
```

You will need [ffmpeg](https://www.ffmpeg.org/download.html) installed on your machine as well.


## Instructions for bleeping your own videos

Start the streamlit demo

```python
python -m streamlit run bleep_that_sht/app.py
```

You will see printouts at the terminal indicating success of the two smallest whisper model downloads - `tiny` and `base`.

Then you can drag and drop your own mp4 (note: only mp4 is accepted) videos into the demo app, define your own bleep_words, and process.

You can download your bleeped video by clicking on the three dots at the bottom right of the bleeped video, and clicking download.
