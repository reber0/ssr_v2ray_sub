#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: reber
@Mail: reber0ask@qq.com
@Date: 2019-12-12 14:42:22
@LastEditTime: 2019-12-12 16:02:22
'''

import sys
sys.dont_write_bytecode = True  # 不生成pyc文件

import base64
import urllib3
import requests
from util import read_file
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_ssr_url():
    def get_ssr_content(url):
        ssr_list = list()
        try:
            resp = requests.get(url=url, verify=False, timeout=5)
            res_list = str(base64.b64decode(resp.text), encoding="utf8")
            for ssr in res_list.split("\n"):
                if ssr.startswith("ssr"):
                    ssr_list.append(ssr)
        except Exception as e:
            print(str(e))
        else:
            return ssr_list

    ssr_list = list()
    urls = [
        "https://raw.githubusercontent.com/ssrsub/ssr/master/ssrsub"
    ]
    for url in urls:
        ssrs = get_ssr_content(url)
        if ssrs:
            ssr_list.extend(ssrs)

    return ssr_list

def get_ssr_txt():
    ssr_list = list()
    ssr_txt = read_file("ssr_pP123PA123Vm.txt")
    for ssr in ssr_txt:
        if ssr.startswith("ssr"):
            ssr_list.append(ssr)

    return ssr_list

def get_ssr():
    ssr_list = list()
    for ssr in get_ssr_url():
        if ssr not in ssr_list:
            ssr_list.append(ssr)
    for ssr in get_ssr_txt():
        if ssr not in ssr_list:
            ssr_list.append(ssr)

    ssr_list = bytes("\n".join(ssr_list), encoding="utf-8")
    return base64.b64encode(ssr_list)
