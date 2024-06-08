import streamlit as st
from bleep_that_sht import main_dir
from bleep_that_sht.transcribe import avaliable_models
from bleep_that_sht.transcribe import transcribe
from bleep_that_sht.audio_extractor import extract_audio
from bleep_that_sht.create import bleep_replace
import tempfile
import io


with st.container(border=True):
    uploaded_file = st.file_uploader("Choose a video...", type=["mp4"])


with st.container(border=True):
    col1, col2, col3 = st.columns([8, 3, 4])
    with col1:
        bleep_words = st.text_area(
            label="bleep-word list",
            placeholder="bleep keywords go here separated by commas",
            value="treetz, ice, cream, chocolate, syrup, cookie, hooked, threats, treats",
        )
    with col2:
        model_selection = st.selectbox(
            label="whisper model",
            placeholder="choose whisper model",
            index=1,
            options=avaliable_models,
        )
    with col3:
        col4 = st.empty()
        with col4:
            st.write("")
            st.write("")
        col5 = st.container()
        with col5:
            trans_button_val = st.button(label="just transcribe", type="secondary")
        col6 = st.container()
        with col6:
            bleep_button_val = st.button(label="transcribe & bleep", type="primary")

a, col0, b = st.columns([1, 20, 1])
colo1, colo2 = st.columns([3, 3])


def button_logic(
    temporary_video_location: str, model_selection: str, bleep_word_list: list
):
    temporary_audio_location = temporary_video_location.replace("mp4", "mp3")
    bleep_video_output = temporary_video_location.replace("original", "bleep")
    bleep_audio_output = bleep_video_output.replace("mp4", "mp3")

    if trans_button_val:
        extract_audio(temporary_video_location, temporary_audio_location)
        transcript, timestamped_transcript = transcribe(
            local_file_path=temporary_audio_location, model=model_selection
        )
        with col0.container(border=True):
            st.text_area(
                value=transcript.strip(),
                placeholder="transcribe text will be shown here",
                label="transcribe text",
            )

    if bleep_button_val:
        extract_audio(temporary_video_location, temporary_audio_location)
        transcript, timestamped_transcript = transcribe(
            local_file_path=temporary_audio_location, model=model_selection
        )

        with col0.container(border=True):
            st.text_area(
                value=transcript.strip(),
                placeholder="transcribe text will be shown here",
                label="transcribe text",
            )

        bleep_replace(
            temporary_video_location,
            temporary_audio_location,
            bleep_video_output,
            bleep_audio_output,
            bleep_word_list,
            timestamped_transcript,
        )

        with colo2:
            st.caption("bleeped video")
            st.video(bleep_video_output)


default_file = main_dir + "/test_data/bleep_test_1.mp4"
if uploaded_file is not None:
    byte_file = io.BytesIO(uploaded_file.read())
else:
    filename = open(default_file, "rb")
    byte_file = io.BytesIO(filename.read())

with tempfile.TemporaryDirectory() as tmpdirname:
    temporary_video_location = tmpdirname + "/" + "original.mp4"
    with open(temporary_video_location, "wb") as out:
        out.write(byte_file.read())
        with st.container(border=True):
            with colo1:
                st.caption("original video")
                st.video(temporary_video_location)
        bleep_word_list = bleep_words.split(",")
        bleep_words_list = [v.strip() for v in bleep_word_list if len(v.strip()) > 0]
        button_logic(temporary_video_location, model_selection, bleep_words_list)
        out.close()
