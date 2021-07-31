# encoding=utf-8
from down_ts import download, get_ts_urls
import os
import subprocess
"""
主程序
"""

def down_m3u8(m3u8_url, video_name,AES_key=None):
    ts_urls = get_ts_urls(m3u8_url)
    cwd,filename = video_name.rsplit('/',1)
    # 创建目录ts_list
    if not os.path.exists(cwd):
        os.mkdir(cwd)
    download(ts_urls, cwd,AES_key=AES_key)

    # 合并ts文件为整个mp4文件，删除ts片段
    subprocess.check_call('cat *.ts>filename.mp4 && rm *.ts', cwd=cwd)
    # linux: cat *.mp4>filename.mp4
    # win:   cp *.mp4>filename.mp4

if __name__ == '__main__':
    m3u8_url = 'https://xxx/index.m3u8'# m3u8_url文件地址
    video_name = "/home/eli/桌面/projects/eli-spiders-all/video-m3u8/ts_list/hello.mp4"# 要保存的文件名
    down_m3u8(m3u8_url, video_name,AES_key="f6e1ee69bacfaecb")