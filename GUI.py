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
        self.window.geometry("1300x550")

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
        self.path_photos = "data/faces_from_camera/"
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

    def GUI_input_name(self):
        self.input_name_box = self.input_name.get()
        self.create_face_folder()
        self.label_faceinstorage['text'] = str(self.existing_faces)

    def delete_previous_data(self):
        # Clears up previous data saved in the folder
        folders_path = os.listdir(self.path_photos)
        for i in range(len(folders_path)):
            shutil.rmtree(self.path_photos + folders_path[i])
        if os.path.isfile("data/features_all.csv"):
            os.remove("data/features_all.csv")
        self.label_faceinstorage['text'] = "0"
        self.existing_faces_cnt = 0
        self.log_total["text"] = "Photos and their`.csv` files are removed!"

    def save_current_photo(self):
        if self.face_folder_created_flag:
            if self.current_frame_faces_cnt == 1:
                if not self.out_of_range_flag:
                    self.ss += 1
                    # Create blank image according to the size of face detected
                    self.face_ROI_image = np.zeros((int(self.face_ROI_height * 2), self.face_ROI_width * 2, 3),
                                                   np.uint8)
                    for ii in range(self.face_ROI_height * 2):
                        for jj in range(self.face_ROI_width * 2):
                            self.face_ROI_image[ii][jj] = self.current_frame[self.face_ROI_height_start - self.hh + ii][
                                self.face_ROI_width_start - self.ww + jj]
                    self.log_total["text"] = "\"" + self.current_face_path + "/img_face_" + str(
                        self.ss) + ".png\"" + " saved!"
                    self.face_ROI_image = cv2.cvtColor(self.face_ROI_image, cv2.COLOR_BGR2RGB)

                    cv2.imwrite(self.current_face_path + "/img_face_" + str(self.ss) + ".png", self.face_ROI_image)
                    logging.info("%-40s %s/img_face_%s.p", "Save into：",
                                 str(self.current_face_path), str(self.ss) + ".png")
                else:
                    self.log_total["text"] = "Face out of range!"
            else:
                self.log_total["text"] = "No face in frame!"
        else:
            self.log_total["text"] = "Please register in step 2first!"

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
                  command=self.GUI_input_name).grid(row=8, column=2, padx=5)

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

        # 新建保存人脸图像文件和数据 CSV 文件夹 / Mkdir for saving photos and csv
    
    def Folders(self):
        # Create folders to save face images and csv
        if os.path.isdir(self.path_photos):
            pass
        else:
            os.mkdir(self.path_photos)

    # If there are already people registered in the folder start from person_x+1
    def check_existing_faces_cnt(self):
        if os.listdir("data/data_faces_from_camera/"):
            # Obtain the number of latest person
            person_list = os.listdir("data/data_faces_from_camera/")
            person_num_list = []
            for person in person_list:
                person_order = person.split('_')[1].split('_')[0]
                person_num_list.append(person_order)
            self.existing_faces_cnt = max(person_num_list)

        # If no one has registered before, start from person_1
        else:
            self.existing_faces_cnt = 0

    # Update FPS of Video stream
    def update_fps(self):
        now = time.time()
        if str(self.start_time).split(".")[0] != str(now).split(".")[0]:
            self.fps_show = self.fps
        self.start_time = now
        self.frame_time = now - self.frame_start_time
        self.fps = 1.0 / self.frame_time
        self.frame_start_time = now

        self.label_fps["text"] = str(self.fps.__round__(2))
    def get_frame(self):
            try:
                if self.cap.isOpened():
                    ret, frame = self.cap.read()
                    return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            except:
                print("Error: No video input!!!")

    # Main function for face detection and saving
    def process(self):
        ret, self.current_frame = self.get_frame()
        faces = detector(self.current_frame, 0)
        # Get frame
        if ret:
            self.update_fps()
            self.label_face_in_frame["text"] = str(len(faces))
            # Face detected
            if len(faces) != 0:
                # Show the ROI of faces
                for k, d in enumerate(faces):
                    self.face_ROI_width_start = d.left()
                    self.face_ROI_height_start = d.top()
                    # Compute the size of rectangle box
                    self.face_ROI_height = (d.bottom() - d.top())
                    self.face_ROI_width = (d.right() - d.left())
                    self.hh = int(self.face_ROI_height / 2)
                    self.ww = int(self.face_ROI_width / 2)

                    # If the size of ROI > 480x640, output "out of range"
                    if (d.right() + self.ww) > 640 or (d.bottom() + self.hh > 480) or (d.left() - self.ww < 0) or (
                            d.top() - self.hh < 0):
                        self.label_warning["text"] = "OUT OF RANGE"
                        self.label_warning['fg'] = 'red'
                        self.out_of_range_flag = True
                        color_rectangle = (255, 0, 0)
                    else:
                        self.out_of_range_flag = False
                        self.label_warning["text"] = ""
                        color_rectangle = (255, 255, 255)
                    self.current_frame = cv2.rectangle(self.current_frame,
                                                       tuple([d.left() - self.ww, d.top() - self.hh]),
                                                       tuple([d.right() + self.ww, d.bottom() + self.hh]),
                                                       color_rectangle, 2)
            self.current_frame_faces_cnt = len(faces)

            # Convert PIL.Image.Image to PIL.Image.PhotoImage
            img_Image = Image.fromarray(self.current_frame)
            img_PhotoImage = ImageTk.PhotoImage(image=img_Image)
            self.label.img_tk = img_PhotoImage
            self.label.configure(image=img_PhotoImage)

        # Refresh frame
        self.window.after(20, self.process)

    def run(self):
        self.Folders()
        self.check_existing_faces_cnt()
        self.GUI_info()
        self.process()
        self.window.mainloop()


def main():
    logging.basicConfig(level=logging.INFO)
    Face_Register_con = Face_Register()
    Face_Register_con.run()


if __name__ == '__main__':
    main()
