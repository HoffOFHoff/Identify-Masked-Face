import dlib
import numpy as np
import cv2
import os
import shutil
import time
import logging
import tkinter as tk
from tkinter import Label, font as tkFont
from PIL import Image, ImageTk

#Use the front camera face detector function of Dlib
detector = dlib.get_frontal_face_detector()

class Face_Register:
    def __init__(self):

        self.current_frame_faces = 0  # Counting faces in current frame
        self.existing_faces = 0  # Counting saved faces
        self.ss = 0  # Get screen shots

        #Obtaining GUI
        self.window = tk.Tk()
        self.window.title("Face Recognition")

        # The window size could be modified here.
        self.window.size("1000*1000")

        # left side of the GUI
        self.frame_left = tk.Frame(self.window)
        self.label = tk.Label(self.window)
        self.label.pack(side=tk.LEFT)
        self.frame_left.pack()

        # right side of the GUI
        self.frame_right = tk.Frame(self.window)
        self.label_faceinstorage = tk.Label(self.frame_right, text=str(self.existing_faces))
        self.label_fps = tk.Label(self.frame_right, text="")
        self.input_name = tk.Entry(self.frame_right)
        self.input_name_char = ""
        self.label.face = tk.Label(self.frame_right, text="Faces in frame belongs to:")
        self.log_total = tk.Label(self.frame_right)
        self.label_warning = tk.Label(self.frame_right)

        # Font settings for the GUI
        self.font_title = tkFont.Font(family='Helvetica', size=25, weight='bold')
        self.font_step_title = tkFont.Font(family='Helvetica', size=15, weight='bold')
        self.font_warning = tkFont.Font(family='Helvetica', size=15, weight='bold')
        self.font = cv2.FONT_HERSHEY_COMPLEX

        # Pathway setting for the GUI
        self.path_photos = "data/faces_from_camera"
        self.current_face_path = ""

        # Current frame and face ROI position
        self.current_frame = np.ndarray
        self.face_ROI_image = np.ndarray
        self.face_ROI_width_start = 0
        self.face_ROI_height_start = 0
        self.face_ROI_width = 0
        self.face_ROI_height = 0
        self.ww = 0
        self.hh = 0

        # Flag rising occations
        self.out_of_range_flag = False
        self.face_folder_created_flag = False
        
        # Obtaining FPS
        self.frame_time = 0
        self.frame_start_time = 0
        self.fps = 0
        self.fps_show = 0
        self.start_time = time.time()

        # Obtaining video stream from camera
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 180)
        self.cap.set(cv2.CAP_PROP_FPS, 25)



