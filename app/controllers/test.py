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

#这个完整路径是 /test/
#try: curl http://127.0.0.1:5000/test/
@module.route('/')
def index():
    return jsonify(code=0, message='This is ' + module_name)

#这个完整路径是 /test/test
#try:
#   curl http://127.0.0.1:5000/test/test
#   curl http://127.0.0.1:5000/test/test -d 'q=xxx'
@module.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('test/test.html', method=request.method)

#这个完整路径是 /test/get?q=xxx
#try: curl http://127.0.0.1:5000/test/get?q=xxx
@module.route('/get', methods=['GET'])
def get():
    message = 'q = %s' % (request.args.get('q', ''))
    return jsonify(code=0, message=message)

#这个完整路径是 /test/post
#try: curl http://127.0.0.1:5000/test/post -d 'q=xxx'
@module.route('/post', methods=['POST'])
def post():
    message = 'q = %s' % (request.form['q'])
    return jsonify(code=0, message=message)

#这个完整路径是 /test/arg/<q>
#try: curl http://127.0.0.1:5000/test/arg/xxx?q=yyy
@module.route('/arg/<p>', methods=['GET'])
def arg(p):
    message = 'p = %s, q = %s' % (p, request.args.get('q', ''))
    return jsonify(code=0, message=message)
