#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:eli
# datetime:2021/8/4 上午11:50
"""
# ffmpeg 提取视频中的音频
# ffmpeg -i D:\AI\bili_data\test.mp4 -vn -y -acodec copy D:\AI\bili_data\output.mp3

# moviepy 提取视频中的音频
# from moviepy.editor import AudioFileClip
# my_audio_clip = AudioFileClip("e:/chrome/my_video.mp4")
# my_audio_clip.write_audiofile("e:/chrome/my_audio.wav")

"""

from moviepy.editor import AudioFileClip
import os



def main_parse():
    filenames = os.listdir('./videos')
    for f in filenames:
        my_audio_clip = AudioFileClip("./videos/"+f)
        my_audio_clip.write_audiofile("./audios/{}.mp3".format(f))


if __name__ == '__main__':
    main_parse()
