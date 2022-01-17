# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name :     get_driver
   Description :   
   Author :       clever
   date：          2022/1/14
-------------------------------------------------
   Change Activity:
                   2022/1/14 22:50: 
-------------------------------------------------
"""
__author__ = 'clever'


def get_driver():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('--no-sandbox')
    # 指定浏览器分辨率
    # chrome_options.add_argument('window-size=1920x3000')
    # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--disable-gpu')
    # 隐藏滚动条, 应对一些特殊页面
    chrome_options.add_argument('--hide-scrollbars')
    # 不加载图片, 提升速度
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    chrome_options.add_argument('--headless')
    # 手动指定本机电脑使用的浏览器位置,非必要不建议自己指定,容易出错
    # chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

    # 创建一个driver,进行后面的请求页面等操作，executable_path指定本机中chromedriver.exe的位置
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="./tools/chromedriver.exe")
    return driver
