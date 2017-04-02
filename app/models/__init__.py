#coding:utf-8

import os
import sys
import glob

G = globals()

model_files = glob.glob('app/models/*.py')
for filename in model_files:
    basename = os.path.basename(filename)
    model_name = basename[0:basename.find('.')]
    if model_name == '__init__':
        continue
    sys.stderr.write('from .%s import %s\n' % (model_name, model_name))
    module = __import__('app.models.' + model_name, fromlist=[model_name])
    G[model_name] = getattr(module, model_name)
