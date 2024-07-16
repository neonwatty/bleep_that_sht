from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from pydub import AudioSegment
from bleep_that_sht import base_dir
from bleep_that_sht.audio_extractor import extract_audio

bleep_sound = AudioSegment.from_mp3(base_dir + "/bleep.mp3")
bleep_first_sec = bleep_sound[1 * 1000 : 2 * 1000]


# simple word cleaner - remove punctuation etc.,
def word_cleaner(word: str) -> str:
    return "".join(e for e in word if e.isalnum()).lower().strip()


# collect all timestamped instances of bleep_word in transcript
def query_transcript(bleep_words: list, timestamped_transcript: list) -> list:
    transcript_words = sum(
        [timestamped_transcript[i]["words"] for i in range(len(timestamped_transcript))],
        [],
    )
    detected_bleep_words = []
    for bleep_word in bleep_words:
        detected_bleep_words += [v for v in transcript_words if word_cleaner(v["text"]) == word_cleaner(bleep_word)]
    detected_bleep_words = sorted(detected_bleep_words, key=lambda d: d["start"])
    return detected_bleep_words


def bleep_replace(
    og_video_path: str,
    og_audio_path: str,
    final_video_path: str,
    final_audio_path: str,
    bleep_words: list,
    timestamped_transcript: dict,
) -> None:
    # # extract and save audio from original video
    # extract_audio(local_file_path=og_video_path, audio_filepath=og_audio_path)

    # input og audio file for splicing
    test_sound = AudioSegment.from_mp3(og_audio_path)

    # find bleep_words in timestamped transcript
    bleep_word_instances = query_transcript(bleep_words, timestamped_transcript)

    # start creation of test_sound_bleeped - by splicing in instance 0
    test_clip = test_sound[:1]
    test_sound_clips = [test_clip]

    # loop over instances, thread in clips of bleep
    prev_end_time = 1
    for instance in bleep_word_instances:
        # unpack bleep_word start / end times - converted to microseconds
        start_time = int(instance["start"] * 1000) - 50
        end_time = int(instance["end"] * 1000) + 50

        # collect clip of test starting at previous end time, and leading to start_time of next bleep
        test_clip = test_sound[prev_end_time:start_time]

        # create bleep clip for this instance
        bleep_clip = bleep_first_sec[: (end_time - start_time)]

        # store test and bleep clips
        test_sound_clips.append(test_clip)
        test_sound_clips.append(bleep_clip)

        # update prev_end_time
        prev_end_time = end_time

    # create final clip from test
    test_clip = test_sound[prev_end_time:]
    test_sound_clips.append(test_clip)

    # save bleeped audio
    bleeped_test_clip = sum(test_sound_clips)
    bleeped_test_clip.export(final_audio_path, format="mp3")

    # load in og video, overlay with bleeped audio
    og_video = VideoFileClip(og_video_path)
    bleep_audio = AudioFileClip(final_audio_path)
    new_audioclip = CompositeAudioClip([bleep_audio])
    og_video.audio = new_audioclip
    og_video.write_videofile(
        final_video_path,
        codec="libx264",
        audio_codec="aac",
        temp_audiofile="temp-audio.m4a",
        remove_temp=True,
    )
