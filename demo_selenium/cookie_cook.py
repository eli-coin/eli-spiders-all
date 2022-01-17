# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name :     cookie_cook
   Description :   
   Author :       clever
   date：          2022/1/17
-------------------------------------------------
   Change Activity:
                   2022/1/17 23:23: 
-------------------------------------------------
"""
__author__ = 'clever'

import time

from get_driver import get_driver


def do_baidu():
    driver = get_driver()  # 设置driver 模拟浏览器程序
    # driver.set_window_size(300,200) # ！注意，window_size遮住的按钮，是不可以实现模拟鼠标点击操作的。
    driver.get("https://www.baidu.com")  # 模拟浏览器访问url
    time.sleep(2)

    # 操作cookie
    # 查看源文档add_cookie
    cookie = {'name': 'eli-coin', 'value': '123456790'}
    driver.add_cookie(cookie)

    cookies = driver.get_cookies()
    for cookie in cookies:
        print(cookie)

    time.sleep(2)  # ！此处sleep不仅是为了观察，还为了足够的时间使driver.page_source的更新
    driver.close()  # 关闭模拟器
    driver.quit()


if __name__ == '__main__':
    do_baidu()
