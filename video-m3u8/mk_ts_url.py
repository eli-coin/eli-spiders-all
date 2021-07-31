# encoding=utf-8
import requests
from urllib import parse
from config import headers
"""
从m3u8文件中提取ts文件的url
"""

def get_ts_urls(m3u8_url):
    urls = []
    file_name = m3u8_url.split("/")[-1]
    base_url = m3u8_url.strip(file_name)
    r = requests.get(m3u8_url,headers=headers)
    lines = r.text.split('\n')
    for line in lines:
        if line.endswith(".ts"):
            urls.append(parse.urljoin(base_url,line.strip("\n")))
    return urls


if __name__ == '__main__':
    m3u8_url = 'https://xxxx/index.m3u8'
    ts_url_list = get_ts_urls(m3u8_url)
    print("\n".join(ts_url_list))