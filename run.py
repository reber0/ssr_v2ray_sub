#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: reber
@Mail: reber0ask@qq.com
@Date: 2019-12-02 10:41:40
@LastEditTime: 2019-12-12 16:15:27
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


if __name__=='__main__':
    app.run(host='0.0.0.0', port=2280, debug=False)

