from cv2 import cv2
import matplotlib.pyplot as plt
import os
from datetime import timedelta
from lib.utility import enforce_int


def get_frame_dimensions(filepath):
    if os.path.exists(filepath):
        frame = cv2.imread(filepath)
        h, w, l = frame.shape
        return w, h
    return 10, 10


def get_filepath(src, filename):
    return f"{src}{filename}"


def render_graph_anim(fps, src="img/anim/", target="out.avi"):
    images = [f for f in os.listdir(src) if os.path.isfile(os.path.join(src, f))]
    if not len(images):
        return

    print(f"...rendering {target}")
    w, h = get_frame_dimensions(get_filepath(src, images[0]))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(target, fourcc, enforce_int(fps), (w, h))
    
    for f in images:
        filepath = get_filepath(src, f)
        image = cv2.imread(filepath)
        video.write(image)
    
    video.release()