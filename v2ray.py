#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: reber
@Mail: reber0ask@qq.com
@Date: 2019-12-02 10:41:40
@LastEditTime: 2019-12-11 16:04:22
'''

import sys
sys.dont_write_bytecode = True  # 不生成pyc文件

import base64
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
import requests
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
        "https://raw.githubusercontent.com/eycorsican/rule-sets/master/kitsunebi_sub"
    ]
    for url in urls:
        v2rays = get_v2ray_content(url)
        if v2rays:
            v2ray_list.extend(v2rays)

    return v2ray_list

def get_v2ray_txt():
    def read_file(filename):
        data = list()
        with open(filename,'r') as f:
            for line in f.readlines():
                data.append(line.strip())
        return data

    v2ray_list = list()
    v2ray_txt = read_file("6234jy123t.txt")
    for v2ray in v2ray_txt:
        if v2ray.startswith("vmess"):
            v2ray_list.append(v2ray)

    return v2ray_list


app = Flask(__name__)

@app.route("/v2ray")
def v2ray():
    key = request.args.get("key")
    if key == "Y12358n123":
        v2ray_list = list()
        for v2ray in get_v2ray_url():
            if v2ray not in v2ray_list:
                v2ray_list.append(v2ray)
        for v2ray in get_v2ray_txt():
            if v2ray not in v2ray_list:
                v2ray_list.append(v2ray)

        v2ray_list = bytes("\n".join(v2ray_list), encoding="utf-8")
        return base64.b64encode(v2ray_list)
    else:
        return "error"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=2280, debug=False)
