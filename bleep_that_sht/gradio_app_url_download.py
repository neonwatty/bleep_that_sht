from bleep_that_sht import main_dir
from bleep_that_sht.transcribe import avaliable_models
from bleep_that_sht.transcribe import transcribe
from bleep_that_sht.audio_extractor import extract_audio
from bleep_that_sht.create import bleep_replace
from bleep_that_sht.yt_download import download_video
import tempfile
import uuid
import os
import io
import gradio as gr


HF_TOKEN = None

try:
    HF_TOKEN = os.environ.get("HF_TOKEN")
except:
    pass


print("Setting up Gradio interface...")
with gr.Blocks(theme=gr.themes.Soft(), title="🎬 Bleep That Sh*t 🙊") as demo:
    with gr.Tabs():
        with gr.TabItem("🎬 Bleep That Sh*t 🙊"):
            with gr.Row():
                with gr.Column(scale=4):
                    url_input = gr.Textbox(
                        value="https://www.youtube.com/shorts/43BhDHYBG0o",
                        label="🔗 Paste YouTube / Shorts URL here",
                        placeholder="e.g., https://www.youtube.com/watch?v=.",
                        max_lines=1,
                    )

            with gr.Row():
                with gr.Column(scale=8):
                    bleep_words = gr.Textbox(
                        placeholder="bleep keywords go here separated by commas",
                        label="bleep-word list",
                        value="treetz, ice, cream, chocolate, syrup, cookie, hooked, threats, treats, trees",
                    )
                with gr.Column(scale=3):
                    gr.Dropdown(choices=avaliable_models, value=1, label="whisper model (base only in HF space)", info="whisper model selection")
                with gr.Column(scale=4):
                    just_transcribe_button = gr.Button("Just Transcribe", variant="primary")
                    bleep_transcribe_button = gr.Button("Transcribe & Bleep", variant="primary")

            with gr.Row():
                transcript_output = gr.Textbox(label="Video Transcript", placeholder="", max_lines=5, show_copy_button=True)

                og_video = gr.Video(
                    show_download_button=True,
                    show_label=True,
                    label="original video",
                    format="mp4",
                    visible=True,
                    width="50vw",
                    height="50vw",
                )
                            
                bleep_video = gr.Video(
                    show_download_button=True,
                    show_label=True,
                    label="bleeped video",
                    format="mp4",
                    visible=True,
                    width="50vw",
                    height="50vw",
                )


            @just_transcribe_button.click(inputs=[url_input, transcript_output], outputs=[og_video, transcript_output])
            def just_transcribe(url_input, transcript_output):
                with tempfile.TemporaryDirectory() as tmpdirname:
                    temporary_video_location = tmpdirname + "/original_" + str(uuid.uuid4()) + ".mp4"
                    download_video(url_input, temporary_video_location)
                    filename = open(temporary_video_location, "rb")
                    byte_file = io.BytesIO(filename.read())
                    with open(temporary_video_location, "wb") as out:
                        out.write(byte_file.read())
                        og_video.value = temporary_video_location
                     
                    transcript_output = ""

    with gr.Tab("💡 About"):
        with gr.Blocks() as about:
            gr.Markdown(
                (
                    "### Bleep out words of your choice from an input video.  \n"
                    "How it works: \n\n"
                    "1.  Provided a youtube / shorts url \n"
                    "2.  Choose your your desired bleep keywords \n"
                    "3.  (if running locally) Choose a model from the Whisper family to transcribe the audio (defaults to base only for HF space) \n"
                    "4.  (optional) Press 'Just Transcribe' to examine / download just the transcription of the video (can help in choosing bleep words) \n"
                    "5.  Press 'Transcribe and bleep' to transcribe and replace all instances of your keywords with *beep* sounds \n\n"
                    "If you want to select your Whisper model / run longer videos pull and run the app locally. \n\n"
                    "Notice: baseline (not fine tuned) Whisper models are used here - you may need to be creative to bleep out all the versions of an input word you want depending on its transcription. \n\n"
                    "You do *not* need a GPU to run this locally.  Larger models take more time to process locally, but its doable. \n"
                )
            )

        # print(f"local_file_path --> {local_file_path}")

        # if local_file_path is not None:
        #     og_video = gr.PlayableVideo(
        #         value=local_file_path,
        #         show_download_button=True,
        #         show_label=True,
        #         label="bleeped video",
        #         visible=True
        #     )

        # with gr.Row():
        #     with gr.Column():
        #         bleep_words = gr.Textbox(
        #             placeholder="bleep keywords go here separated by commas",
        #             label="bleep-word list",
        #             value="treetz, ice, cream, chocolate, syrup, cookie, hooked, threats, treats",
        #         )

        #     with gr.Column():
        #         model_selection = gr.Dropdown(
        #             avaliable_models,
        #             label="base",
        #             info="Whisper models - small to large",
        #         )

        #     just_transcribe_button = gr.Button("Just Transcribe", variant="primary")
        #     bleep_transcribe_button = gr.Button("Transcribe & Bleep", variant="primary")

        # with gr.Column():
        #     transcription_output = gr.Textbox(
        #         label="Transcription", lines=10, show_copy_button=True
        #     )
        # with gr.Column():
        #     timestamped_transcription_output = gr.Textbox(
        #         label="Timestamped Transcription", lines=10, show_copy_button=True
        #     )

        # with gr.Column():
        #     og_video = gr.PlayableVideo(
        #         value=None,
        #         show_download_button=True,
        #         show_label=True,
        #         label="bleeped video",
        #     )

        # with tempfile.TemporaryDirectory() as tmpdirname:
        #     temporary_video_location = tmpdirname + "/" + "original.mp4"
        #     temporary_audio_location = temporary_video_location.replace("mp4", "mp3")

        #     bleep_video_output = temporary_video_location.replace("original", "bleep")
        #     bleep_audio_output = bleep_video_output.replace("mp4", "mp3")

        #     def download(url: str,
        #                  tmpdirname: str) -> str | None:
        #         if len(url) > 0:
        #             local_file_path = download_video(url, tmpdirname)
        #             return local_file_path
        #         else:
        #             return None

        # just_transcribe_button.click(
        #     just_transcribe,
        #     inputs=[
        #         temporary_video_location,
        #         temporary_audio_location,
        #         model_selection,
        #     ],
        #     outputs=[transcription_output, timestamped_transcription_output],
        # )

        # with gr.Column():
        #     bleep_video = gr.PlayableVideo(
        #         value=bleep_video_output,
        #         show_download_button=True,
        #         show_label=True,
        #         label="bleeped video",
        #     )

        # just_transcribe_button.click(
        #     just_transcribe,
        #     inputs=[
        #         temporary_video_location,
        #         temporary_audio_location,
        #         model_selection,
        #     ],
        #     outputs=[transcription_output, timestamped_transcription_output],
        # )

        # bleep_transcribe_button.click(
        #     transcribe_and_bleep,
        #     inputs=[
        #         temporary_video_location,
        #         temporary_audio_location,
        #         bleep_video_output,
        #         bleep_audio_output,
        #         model_selection,
        #         bleep_words,
        #     ],
        #     outputs=[transcription_output, timestamped_transcription_output],
        # )

if __name__ == "__main__":
    print("Launching Gradio interface...")
    demo.launch()
