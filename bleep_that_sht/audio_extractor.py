from moviepy.editor import VideoFileClip


def extract_audio(local_file_path: str, audio_filepath: str) -> None:
    try:
        video = VideoFileClip(local_file_path)
        audio = video.audio
        if audio is not None:
            audio.write_audiofile(audio_filepath, verbose=False, logger=None)
            audio.close()
            video.close()
    except Exception as e:
        raise ValueError(f"error extracting audio from video {local_file_path}, exception: {e}")
