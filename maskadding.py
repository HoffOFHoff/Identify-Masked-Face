import os
import numpy as np
from PIL import Image, ImageFile
import face_recognition

IMAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
surgical = os.path.join(IMAGE_DIR, 'surgical.png')
blue = os.path.join(IMAGE_DIR, 'surgical_blue.png')
green = os.path.join(IMAGE_DIR, 'surgical_green.png')
N95 = os.path.join(IMAGE_DIR, 'N95.png')
cloth = os.path.join(IMAGE_DIR, 'cloth.png')


class AddMask:
	