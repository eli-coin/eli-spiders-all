# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name   :     main_rename_file.py
   Description :    根据playlist中的编号,对4k video downloader下载的文件进行按序重命名
   Author :          clever
   date：            2021/12/26
-------------------------------------------------
   Change Activity:
                   2021/12/26 22:01:
-------------------------------------------------
"""
import os
from down_videolist import get_playlist

videos_dir = r"E:\MyTmp\【SDK开发】《Windows程序设计》"
os.chdir(videos_dir) # 改变当前工作目录
file_list = os.listdir("./") # 查看当前目录下的文件
bvid = "BV1us411A7UE" # b站的bvid
page_list, part_list = get_playlist(bvid)
for i in range(len(page_list)):
    print("{}-{}".format(page_list[i], part_list[i]))

for file in file_list:
    file_prename = file.split(".")[0]
    if file_prename in part_list:
        i = part_list.index(file_prename)
        os.renames(file,"{}-{}.mp4".format(page_list[i],part_list[i]))

