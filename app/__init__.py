#!/usr/bin/python
#coding:utf-8

import os
import sys
import time
import csv
import glob
try:
    import simplejson as json
except:
    import json

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    # 注册蓝本
    from app.controllers import module
    app.register_blueprint(module, url_prefix='/')

    module_files = glob.glob('app/controllers/*.py')
    fromlist = []
    for filename in module_files:
        basename = os.path.basename(filename)
        module_name = basename[0:basename.find('.')]
        if module_name == '__init__':
            continue
        fromlist.append(module_name)

    package = __import__('app.controllers', fromlist=fromlist)
    for module_name in fromlist:
        module = getattr(package, module_name)
        print >>sys.stderr, 'import module: %s' % module_name
        app.register_blueprint(module.module, url_prefix='/' + module_name)

    # 附加路由和自定义的错误页面
    @app.errorhandler(403)
    def permission_error(error):
        return render_template('error.html', title='Permission Denied', message='you have no permission to view this page'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error.html', title='Page Not Found', message='Sorry, we cannot find this page on server'), 404

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error.html', title='Internel Server Error', message='Server error encounted, please try again later'), 500

    return app
