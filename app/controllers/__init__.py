#coding:utf-8

import os
from flask import Blueprint, request, jsonify, render_template
#from app.models import *
try:
    import simplejson as json
except:
    import json

module_file = os.path.basename(__file__)
module_name = module_file[0:module_file.find('.')]
module = Blueprint(module_name, __name__)

### 以上部分COPY即可 ###

#这个完整路径是 /
@module.route('/')
def index():
    return jsonify(code=0, message='This is /')

#这个完整路径是 /hello
@module.route('hello')
def hello():
    return jsonify(code=0, message='This is /hello')
