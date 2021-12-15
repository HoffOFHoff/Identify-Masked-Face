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
    faces_encodings = []
    faces_names = []
    cur_user = []
    # cur_direc = os.getcwd()
    # path = os.path.join(cur_direc, 'data/faces_from_camera/')


    list_of_files= glob.glob(r"data/faces_from_camera/*/*.png")
    # img_path = list_of_user[0]
    # img_real_path = list_of_user[1]
    number_files = len(list_of_files)
    print(number_files+1)

    for i in range(number_files+1):
        name_user_path = list_of_files[i-1]
        # name_user = re.split(r"[/_]",name_user_path)
        # print(name_user)
        # name_of_user = name_user[6]
        # print(name_of_user)
        # cur_user.append(name_of_user)
        cur_user.append(name_user_path)
    names = list_of_files.copy()


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
        # Display the results
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
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return name

show_the_user()