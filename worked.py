
'''
EN.640.635 Software Carpentry
Final_Project -Identify-Masked-Face-

Part 4.Worked interface 

1. The openCV is used for video capture
2. Draw a rectangle around the face. Input text labels with a name below the face
3. You could find your name is showed under your face. 
4. When you wear mask, it will show name like 'JackMASKED'. 
5. When you do not wear anthing, it will show the first name you type in.
'''

import face_recognition
import cv2
import os
import numpy as np
import glob

import dlib
import csv
from skimage import io
import pandas as pd
import re

def show_the_user():
    '''
    Apply the photo you just took and use it in the video
    capture. It will show the user name.

    **Parameters**

        faces_encodings: *list*
            The encoded face will show as /person_1_name
        face_names: *list*
            The identified name in the first and second GUI
        face_distances: *ndarray*
            The array which is used to describe the difference 
            between two face image
        process_this_frame: *bool*
            When it is false, we stop the video capture process
        best_match_index: *int*
            The face which meet the saved photo best.
        

    **Returns**

        name

    For extra info:

        For face_recognition package:
        *https://github.com/ageitgey/face_recognition
        For OpenCV package:
        *https://opencv.org/opencv-python-is-now-an-official-opencv-project
    '''
    faces_encodings = []
    faces_names = []
    cur_user = []


    list_of_files= glob.glob(r"data/faces_from_camera/*/*.png")
    # we could know that: img_path = list_of_user[0]
    # we could know that: img_real_path = list_of_user[1]
    number_files = len(list_of_files)
    print(number_files+1)

    for i in range(number_files+1):
        name_user_path = list_of_files[i-1]
        # name_user = re.split(r"[/_]",name_user_path)
        # name_of_user = name_user[6]
        cur_user.append(name_user_path)
    names = list_of_files.copy()


    # Append those picture with face_encoding 
    for i in range(number_files):
        globals()['image_{}'.format(i)] = face_recognition.load_image_file(
            list_of_files[i],mode='RGB')
        globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(
            globals()['image_{}'.format(i)])[0]
        faces_encodings.append(globals()['image_encoding_{}'.format(i)])
    # Create array of known names
        names[i] = names[i].replace(cur_user[i], "")
        faces_names.append(names[i])


    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    video_capture = cv2.VideoCapture(0)
    # The comparison start
    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame,number_of_times_to_upsample=1, model='hog')
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(
                    faces_encodings, face_encoding,tolerance=0.3)
                name = "Unknown"
                face_distances = face_recognition.face_distance(
                    faces_encodings, face_encoding)
                
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = faces_names[best_match_index]
                face_names.append(name)

        process_this_frame = not process_this_frame
        # The interface should be adjusted
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Input text label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35),
                        (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)
        # Click q on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return name

show_the_user()