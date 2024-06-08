import os

base_dir = os.path.dirname(os.path.abspath(__file__))
main_dir = os.path.dirname(base_dir)

import whisper_timestamped as whisper

model = whisper.load_model("tiny", device="cpu")
model = whisper.load_model("base", device="cpu")
