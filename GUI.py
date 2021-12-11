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
        self.input_name_box = ""
        self.label_face_in_frame = tk.Label(self.frame_right, text="Faces in frame belongs to:")
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

    def create_face_folder(self):
        # Create a folders for saving faces
        self.existing_faces += 1
        if self.input_name_box:
            self.current_face_path = self.path_photos + \
                                    "person_" + str(self.existing_faces) + "_" + \
                                    self.input_name_box
        else:
            self.current_face_path = self.path_photos + \
                                    "person_" + str(self.existing_faces)
        os.makedirs(self.current_face_path)
        self.log_total["text"] = "\"" + self.current_face_path + "/\" created!"
        logging.info("\n%-40s %s", "Create folders:", self.current_face_path)

        self.ss = 0  # Clear the screen shots
        self.face_folder_created_flag = True  # Face folder already created

    def GUI_get_input_name(self):
        self.input_name_box = self.input_name.get()
        self.create_face_folder()
        self.label_faceinstorage['text'] = str(self.existing_faces)

    def delete_previous_data(self):
        pass

    def save_current_photo(self):
        pass

    def GUI_info(self):
        tk.Label(self.frame_right,
                 text="Face register",
                 font=self.font_title).grid(row=0, column=0, columnspan=3, sticky=tk.W, padx=2, pady=20)

        tk.Label(self.frame_right,
                 text="FPS: ").grid(row=1, column=0, columnspan=2, sticky=tk.W, padx=5, pady=2)
        self.label_fps.grid(row=1, column=2, sticky=tk.W, padx=5, pady=2)

        tk.Label(self.frame_right,
                 text="Faces in storage: ").grid(row=2, column=0, columnspan=2, sticky=tk.W, padx=5, pady=2)
        self.label_faceinstorage.grid(row=2, column=2, columnspan=3, sticky=tk.W, padx=5, pady=2)

        tk.Label(self.frame_right,
                 text="Faces in current frame: ").grid(row=3, column=0, columnspan=2, sticky=tk.W, padx=5, pady=2)
        self.label_face_in_frame.grid(row=3, column=2, columnspan=3, sticky=tk.W, padx=5, pady=2)

        self.label_warning.grid(row=4, column=0, columnspan=3, sticky=tk.W, padx=5, pady=2)

        # Step 1: Clear old data
        tk.Label(self.frame_right,
                 font=self.font_step_title,
                 text="Step 1: Clear previous photos").grid(row=5, column=0, columnspan=2, sticky=tk.W, padx=5, pady=20)
        tk.Button(self.frame_right,
                  text='Clear',
                  command=self.delete_previous_data).grid(row=6, column=0, columnspan=3, sticky=tk.W, padx=5, pady=2)

        # Step 2: Input name and create folders for photos
        tk.Label(self.frame_right,
                 font=self.font_step_title,
                 text="Step 2: Input your name").grid(row=7, column=0, columnspan=2, sticky=tk.W, padx=5, pady=20)

        tk.Label(self.frame_right, text="Name: ").grid(row=8, column=0, sticky=tk.W, padx=5, pady=0)
        self.input_name.grid(row=8, column=1, sticky=tk.W, padx=0, pady=2)

        tk.Button(self.frame_right,
                  text='Input',
                  command=self.delete_previous_data).grid(row=8, column=2, padx=5)

        # Step 3: Save current face in frame
        tk.Label(self.frame_right,
                 font=self.font_step_title,
                 text="Step 3: Save face image").grid(row=9, column=0, columnspan=2, sticky=tk.W, padx=5, pady=20)

        tk.Button(self.frame_right,
                  text='Save current face',
                  command=self.save_current_photo).grid(row=10, column=0, columnspan=3, sticky=tk.W)

        # Show log in GUI
        self.log_total.grid(row=11, column=0, columnspan=20, sticky=tk.W, padx=5, pady=20)

        self.frame_right.pack()


