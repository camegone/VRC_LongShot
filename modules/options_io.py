import os
import sys
import json

option_path = 'options.json'

def load(app_version=0):
    need_refresh = False
    #if options not exist, create new one
    if not os.path.isfile(option_path):
        create_file(app_version)
    
    options = dict()
    with open(option_path, mode='r', encoding='utf-8') as f:
        options = json.load(f)
        
    if 'version' not in options or options['version'] < app_version:
        need_refresh = True
    
    if need_refresh:
        create_file(app_version, options)
        options = load(app_version)
    
    return options
    
def save(op_json):
    with open(option_path, mode='w', encoding='utf-8') as f:
        json.dump(op_json, f, indent=2)
    

def create_file(app_version=0, options=dict()):
    options['version'] = app_version
    #capture
    options.setdefault('capture', dict())
    options['capture'].setdefault('target', 'VRChat')
    options['capture'].setdefault('fps', 10)
    options['capture'].setdefault('seconds', 10)
    options['capture'].setdefault('force_focused', True)
    options['capture'].setdefault('resize', True)
    #resize
    options['capture'].setdefault('size', dict())
    options['capture']['size'].setdefault('width', 1280)
    options['capture']['size'].setdefault('height', 720)
    #save
    options.setdefault('save', dict())
    options['save'].setdefault('folder', 'photos/')
    options['save'].setdefault('prefix', 'VRCLS')
    options['save'].setdefault('monthly_subdir', True)
    options['save'].setdefault('make_bright', True)
    
    save(options)
