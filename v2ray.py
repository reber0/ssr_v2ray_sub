#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: reber
@Mail: reber0ask@qq.com
@Date: 2019-12-12 14:40:22
@LastEditTime: 2019-12-12 16:05:22
'''

import sys
sys.dont_write_bytecode = True  # 不生成pyc文件

import base64
import requests
from util import read_file
requests.packages.urllib3.disable_warnings()


def get_v2ray_url():
    def get_v2ray_content(url):
        v2ray_list = list()
        try:
            resp = requests.get(url=url, verify=False, timeout=5)
            res_list = str(base64.b64decode(resp.text), encoding="utf8")
            for v2ray in res_list.split("\n"):
                if v2ray.startswith("vmess"):
                    v2ray_list.append(v2ray)
        except Exception as e:
            print(str(e))
        else:
            return v2ray_list

    v2ray_list = list()
    urls = [
        "https://raw.githubusercontent.com/ssrsub/ssr/master/v2ray"
    ]
    for url in urls:
        v2rays = get_v2ray_content(url)
        if v2rays:
            v2ray_list.extend(v2rays)

    return v2ray_list

def get_v2ray_txt():
    v2ray_list = list()
    v2ray_txt = read_file("v2ray_6c345yp829Wt.txt")
    for v2ray in v2ray_txt:
        if v2ray.startswith("vmess"):
            v2ray_list.append(v2ray)

    return v2ray_list

def get_v2ray():
    v2ray_list = list()
    for v2ray in get_v2ray_url():
        if v2ray not in v2ray_list:
            v2ray_list.append(v2ray)
    for v2ray in get_v2ray_txt():
        if v2ray not in v2ray_list:
            v2ray_list.append(v2ray)

    v2ray_list = bytes("\n".join(v2ray_list), encoding="utf-8")
    return base64.b64encode(v2ray_list)
