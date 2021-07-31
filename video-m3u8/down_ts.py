# encoding=utf-8

import datetime
import requests
from mk_ts_url import get_ts_urls
from decrpyt import aes_decode
from config import headers
"""
下载视频片段ts文件
"""


def download(ts_urls:list, download_path,AES_key=None):
    """
    :param ts_urls:
    :param download_path:
    :param AES_key: ts片段AES解密的key,若未加密则为None
    :return:
    """
    for i in range(len(ts_urls)):
        ts_url = ts_urls[i]
        try:
            response = requests.get(ts_url,stream=True,headers=headers)
        except Exception as e:
            print("异常请求：%s" % e.args)
            return

        ts_path = download_path + "/{0}.ts".format(i)
        with open(ts_path, "wb+") as file:
            chunk = response.content
            if AES_key:
                file.write(aes_decode(chunk,AES_key))
            else:
                file.write(chunk)
        print("总共需下载{}个文件".format(len(ts_urls)),"已下载完成",ts_path)


if __name__ == '__main__':
    m3u8_url = 'https://xxxxx/index.m3u8'
    ts_urls = get_ts_urls(m3u8_url)
    download_path = "ts_list"
    download(ts_urls, download_path,AES_key="f6e1ee69bacfaecb")