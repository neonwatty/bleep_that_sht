from pytube import YouTube
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
            yt = YouTube(url, proxies=my_proxies)
            audio_video_streams = (
                yt.streams.filter(
                    file_extension="mp4",
                    only_audio=False,
                    only_video=False,
                    progressive=True,
                    type="video",
                )
                .order_by("resolution")
                .asc()
            )
            audio_video_itags = [v.itag for v in audio_video_streams]
            first_choice_itag = audio_video_itags[0]
            yt.streams.get_by_itag(first_choice_itag).download(filename=savepath)
            print("...done!")
        else:
            raise ValueError(f"invalid input url: {url}")
    except Exception as e:
        raise ValueError(f"yt_download failed with exception {e}")
