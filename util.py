#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: reber
@Mail: reber0ask@qq.com
@Date: 2019-12-12 14:32:22
@LastEditTime: 2019-12-12 14:32:22
'''

import sys
sys.dont_write_bytecode = True  # 不生成pyc文件

def read_file(filename):
    data = list()
    with open(filename,'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data
