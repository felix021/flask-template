#coding:utf-8

import os
from flask import Blueprint, request, jsonify, render_template
from app import db
from app.models import *
try:
    import simplejson as json
except:
    import json

module_file = os.path.basename(__file__)
module_name = module_file[0:module_file.find('.')]
module = Blueprint(module_name, __name__)

### 以上部分COPY即可 ###

def user_as_dict(user):
    return {'id': user.id, 'name': user.Username, 'age': user.Age}

#这个完整路径是 /user/
@module.route('/')
def user_index():
    users = User.query.all()
    user_list = []
    for user in users:
        user_list.append(user_as_dict(user))
    return jsonify(code=0, message='ok', data=user_list)

#这个完整路径是 /user/detail/<username>
@module.route('/detail/<username>')
def user_detail(username):
    user = User.query.filter_by(Username=username).first()
    if user:
        return jsonify(code=0, message='ok', data=user_as_dict(user))
    else:
        return jsonify(code=1, message='not found', data={})

#这个完整路径是 /user/add
@module.route('/add', methods=['POST'])
def user_add():
    username = request.form['username']
    password = request.form['password']
    age      = int(request.form['age'])
    user = User(username, password, age)
    db.session.add(user)
    db.session.commit()
    return jsonify(code=0, message='user created', data=user_as_dict(user))
