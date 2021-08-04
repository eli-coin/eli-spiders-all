#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:eli
# datetime:2021/8/4 下午12:21
# software: PyCharm
"""
from pydub import AudioSegment  # 先导入这个模块
import os
filems = os.listdir("D:/1/mp3/mp3")
dirj = "D:/1/mp3/mp3/"
dirjl = "D:/1/mp3/mp4/"
index=0
for f in filems:
    input_music = AudioSegment.from_mp3(dirj+f) # 加载mp3音频
    output_music = input_music[:9000] # 截取音频的前3秒(单位为毫秒)
    #output_music = input_music[9000:] # 截取音频的最后3秒(单位为毫秒)
    #fary = f.split(".")
    #name = fary[0]+str(index)+"."+fary[1]
    output_music.export(dirjl+f, format="mp3") # 保存音频，前面为保存的路径，后面为保存的格式

"""


"""
from pydub import AudioSegment
from pydub.utils import make_chunks
 
myaudio = AudioSegment.from_file("myAudio.wav" , "wav") 
chunk_length_ms = 1000 # 分块的毫秒数
chunks = make_chunks(myaudio, chunk_length_ms) #将文件切割成1秒每块
 
#保存切割的音频到文件
 
for i, chunk in enumerate(chunks):
    chunk_name = "chunk{0}.wav".format(i)
    print "exporting", chunk_name
    chunk.export(chunk_name, format="wav")


mp3 = AudioSegment.from_mp3(filename) # 打开mp3文件
mp3[17*1000+500:].export(filename, format="mp3") # 切割前17.5秒并覆盖保存
"""

import os
from pydub import AudioSegment
from pydub.utils import make_chunks

def cuts_mp3(filename):
    myaudio = AudioSegment.from_file(filename, "mp3")
    chunk_length_ms = 1000 * 60 * 10  # 分块的毫秒数 (10分钟)
    chunks = make_chunks(myaudio, chunk_length_ms)  # 将文件切割成10分钟每块

    # 保存切割的音频到文件
    for i, chunk in enumerate(chunks):
        chunk_name = "{}-[{}].mp3".format(filename.replace('.mp3','').replace('audios','mp3cuts'),i)
        print("exporting", chunk_name)
        chunk.export(chunk_name, format="mp3")


def main_cuts():
    filenames = os.listdir('./audios/')
    for f in filenames:
        cuts_mp3("./audios/"+f)


if __name__ == '__main__':
    main_cuts()
