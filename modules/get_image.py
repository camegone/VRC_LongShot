from . import window_handler as wh

import numpy as np
import pyautogui as pag
import sys
import os
from PIL import Image

Gimage = None
Gframes = 0

def init():
    global Gimage
    global Gframes
    
    Gimage = None
    Gframes = 0

def add_frame(target_name=None):
    global Gimage
    global Gframes
    
    img = pag.screenshot(region=wh.get_area(target_name))
    Gframes += 1
    
    if Gimage is None:
        Gimage = np.array(img)
        Gimage = Gimage.astype(np.uint32)
    else:
        Gimage = Gimage + np.array(img)

def write(file_name, bright=True):
    print('processing...')
    if Gimage is None:
        sys.exit(1)
    
    if bright:
        img = Gimage / ((np.amax(Gimage) + 1) / 255)
    else:
        img = Gimage / Gframes
    img = img.astype(np.uint8)
    
    photo = Image.fromarray(img)
    photo.save(file_name)
    print(f'photo saved in: {file_name}')

def get_size():
    if Gimage is None:
        sys.exit(1)
    
    print(f'shape: {Gimage.shape}')
    return {'height': Gimage.shape[0], 'width': Gimage.shape[1]}

def ensure_dir(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)