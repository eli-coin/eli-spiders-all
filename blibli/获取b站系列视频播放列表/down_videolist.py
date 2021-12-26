# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     down_videolist.py
   Description :    根据B站API下载pagelist的json数据,并解析
   Author :       clever
   date：          2021/12/26
-------------------------------------------------
   Change Activity:
                   2021/12/26 22:01:
-------------------------------------------------
"""
import requests
import json, jsonpath

def get_playlist(bvid = "BV1Rs411c7HG"):
    # b_url = "https://www.bilibili.com/video/BV1Rs411c7HG?p=1"
    bvid = bvid
    json_url = "https://api.bilibili.com/x/player/pagelist?bvid={mybvid}&jsonp=jsonp".format(mybvid=bvid)

    pagelist_json = requests.get(json_url).json()

    # print(pagelist_json)

    page_list = jsonpath.jsonpath(pagelist_json, "$.data..page")
    part_list = jsonpath.jsonpath(pagelist_json, "$.data..part")

    # print(len(page_list), len(part_list))

    if len(page_list) == len(part_list):
        # for i in range(len(page_list)):
        #     print("{} {}".format(page_list[i], part_list[i]))
        return page_list,part_list
    else:
        raise "ERROR: len(page_list) != len(part_list)"

if __name__ == '__main__':
    bvid = "BV1Rs411c7HG"
    page_list,part_list = get_playlist(bvid)
    for i in range(len(page_list)):
        print("{} {}".format(page_list[i], part_list[i]))