#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: reber
@Mail: reber0ask@qq.com
@Date: 2019-12-02 10:41:40
@LastEditTime: 2019-12-23 09:56:12
'''

import sys
sys.dont_write_bytecode = True  # 不生成pyc文件

from ssr import get_ssr
from v2ray import get_v2ray
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response


app = Flask(__name__)

@app.route("/ssr")
def ssr():
    key = request.args.get("key")
    if key == "Pv123PEu123Q3612339Efn123RBz123t":
        return get_ssr()
    else:
        return "error"

@app.route("/v2ray")
def v2ray():
    key = request.args.get("key")
    if key == "Hw123T75456yw6543VXUK6545Mt727HH":
        return get_v2ray()
    else:
        return "error"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route("/check/v2ray")
def check_v2ray_txt():
    import base64
    from v2ray import get_v2ray_txt

    key = request.args.get("key")
    if key == "2Pfx1239123":
        v2ray_list = get_v2ray_txt()
        v2ray_list = bytes("\n".join(v2ray_list), encoding="utf-8")
        return base64.b64encode(v2ray_list)

@app.route("/check/ssr")
def check_ssr_txt():
    import base64
    from ssr import get_ssr_txt
    
    key = request.args.get("key")
    if key == "12Pfx1239123":
        ssr_list = get_ssr_txt()
        ssr_list = bytes("\n".join(ssr_list), encoding="utf-8")
        return base64.b64encode(ssr_list)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=2280, debug=False)

