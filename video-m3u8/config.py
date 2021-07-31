#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:eli
@file:config.py
@time:2021/07/31
"""
from faker import Faker
import requests
faker_obj = Faker()
"""
配置文件
"""

use_UA = True # 使用UA
use_ip_proxy = True #使用ip代理
AES = True # 是否AES解密


UA = faker_obj.user_agent() if use_UA else None
# IP_PROXY = "http://127.0.0.1:5010/get?type=https"
# IP_PROXY_PARAM = "proxy"

headers = {'User-Agent': UA}
# ip = requests.get(IP_PROXY).json().get(IP_PROXY_PARAM)
# proxies = {
#     "http": "http://" + ip,
#     "https": "https://" + ip,
# }