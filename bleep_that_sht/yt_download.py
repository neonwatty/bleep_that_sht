# from pytube import YouTube

import yt_dlp
import re


def is_valid_youtube_url(url: str) -> bool:
    if not isinstance(url, str):
        return False
    pattern = r"^https://www\.youtube\.com/watch\?v=[A-Za-z0-9_-]{11}$"  # youtube vido ids are always 11 chars long
    if "shorts" in url:
        pattern = r"^https://www\.youtube\.com/shorts/[A-Za-z0-9_-]{11}$"  # youtube vido ids are always 11 chars long
    return re.match(pattern, url) is not None


def download_video(url: str, savepath: str, my_proxies: dict = {}) -> None:
    try:
        print("Downloading video from youtube...")
        if is_valid_youtube_url(url):
            ydl_opts = {
                "format": "bestvideo[height<=720]+bestaudio/best",
                "merge_output_format": "mp4",
                "outtmpl": savepath,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            print("...done!")
        else:
            raise ValueError(f"invalid input url: {url}")
    except Exception as e:
        raise ValueError(f"yt_download failed with exception {e}")
