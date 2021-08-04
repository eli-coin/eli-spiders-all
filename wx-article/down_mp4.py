#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:eli
# datetime:2021/8/4 上午11:30
# software: PyCharm
import requests

def down(path,title,url):
    r = requests.get(url,stream=True)

    with open(path+title, "wb") as mp4:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                mp4.write(chunk)

    print("finished",title)


def main_down_urls(filename="mp4_urls.txt",path="./videos/"):
    with open(filename,"r") as f:
        for line in f:
            title,url  = line.split("|####|")
            down(path,title,url.strip())

if __name__ == '__main__':
    main_down_urls("./tmp_urls")
