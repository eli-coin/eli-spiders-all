# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name :     exec_js
   Description :   
   Author :       clever
   date：          2022/1/14
-------------------------------------------------
   Change Activity:
                   2022/1/14 22:50: 
-------------------------------------------------
"""
__author__ = 'clever'

from demo_selenium import get_driver

driver = get_driver.get_driver()
driver.get('https://cn.bing.com/images/search?q=%E5%A3%81%E7%BA%B8')
scrool_down_js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(scrool_down_js)  # 使用js,浏览器向下滚动