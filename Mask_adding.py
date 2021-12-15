import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import os
import re

# Load the png file and use face_recognition to get the numpy type
image = face_recognition.load_image_file(
    os.path.join('data/faces_from_camera/person_1_white_hat_ziying/', "img_face_3.png"))

# Find facial features with landmarks function
face_landmarks_list = face_recognition.face_landmarks(image)

# Use PIL imagedraw object to mark points on the face
marked_face = Image.fromarray(image)
signal = ImageDraw.Draw(marked_face)


# Show the location of each facial feature in this image
for face_landmarks in face_landmarks_list:
    # for facial_feature in face_landmarks.keys():
    #     print("The {} in this face has the following points: {}".format(
    #         facial_feature, face_landmarks[facial_feature]))

    # Let's trace out each facial feature in the image with a point!
    for facial_feature in face_landmarks.keys():
        signal.point(face_landmarks[facial_feature])

facelandmarks = []
for key in face_landmarks:
    facelandmarks.append(face_landmarks[key])
# Show the picture with landmarks
marked_face.show()


def mask_img(ori_img_dir, mask_img_dir, facelandmarks):
    """
    :param ori_img_dir: Contains the path of the person's photo
    :param mask_img_dir: Contains the path of a mask photo
    :param facelandmarks: The 72 key points on a human face
    :return: A photo with the person wearing a mask
    """

    # We load in the mask and the person's photo
    # ori_img_dir = "test3.png"
    # mask_img_dir = "surgical.png"
    face_pic = Image.open(ori_img_dir)
    mask_pic = Image.open(mask_img_dir)

    if ".png" in ori_img_dir:
        face_name = re.split("[/.]", ori_img_dir)[-3]
    if ".png" in mask_img_dir:
        mask_type = re.split("[/.]", mask_img_dir)[-2]

    # Obtaining the key points of chin and nose to put on a mask
    nose = facelandmarks[3][1]
    nose_vector = np.array(nose)
    chin_left = facelandmarks[0][1]
    chin_right = facelandmarks[0][15]
    chin_bottom = facelandmarks[0][8]
    chin_bottom_vector = np.array(chin_bottom)

    # We split the mask into left and right and give a factor
    # to stretch the mask
    # to make it suit the face better
    width = mask_pic.width
    height = mask_pic.height
    width_ration = 1.1  # Factor for testing
    # Obtaining the distance between the point on the nose and the point at the bottom of the chin
    new_height = int(np.linalg.norm(nose_vector - chin_bottom_vector))

    # We adjust the left part of the mask，The width is the left point to the middleline * Stretch factor
    mask_left_img = mask_pic.crop((0, 0, width // 2, height))
    # Obtaining the width from the left point to the middleline
    mask_left_width = get_distance_from_point_to_line(
        chin_left, nose, chin_bottom)
    mask_left_width = int(mask_left_width * width_ration)
    mask_left_img = mask_left_img.resize((mask_left_width, new_height))

    # We adjust the right part of the mask，The width is the right point to the middleline * Stretch factor
    mask_right_img = mask_pic.crop((width // 2, 0, width, height))
    # Obtaining the width from the right point to the middleline
    mask_right_width = get_distance_from_point_to_line(
        chin_right, nose, chin_bottom)
    mask_right_width = int(mask_right_width * width_ration)
    mask_right_img = mask_right_img.resize((mask_right_width, new_height))

    # Combine two mask parts
    size = (mask_left_img.width + mask_right_img.width, new_height)
    mask_pic_emp = Image.new('RGBA', size)
    mask_pic_emp.paste(mask_left_img, (0, 0), mask_left_img)
    mask_pic_emp.paste(
        mask_right_img, (mask_left_img.width, 0), mask_right_img)

    # Mask rotation
    angle = np.arctan2(
        chin_bottom[1] - nose[1], chin_bottom[0] - nose[0])
    rotated_mask_pic_emp = mask_pic_emp.rotate(angle, expand=True)

    # We place the mask to the appropriate position
    center_x = (nose[0] + chin_bottom[0]) // 2
    center_y = (nose[1] + chin_bottom[1]) // 2

    Compensation = mask_pic_emp.width // 2 - mask_left_img.width
    radian = angle * np.pi / 180
    box_x = center_x + int(Compensation * np.cos(radian)) - \
        rotated_mask_pic_emp.width // 2
    box_y = center_y + int(Compensation * np.sin(radian)) - \
        rotated_mask_pic_emp.height // 2

    # Adding the mask to the picture
    face_pic.paste(mask_pic_emp, (int(box_x), int(box_y)), mask_pic_emp)
    face_pic.show()
    print("here it is %s, and the mask type is %s" % (face_name, mask_type))
    face_pic.save(os.path.join('data/Masked_faces/', "%s_%s" %
                               (face_name, mask_type) + ".png"))
    return face_pic


def get_distance_from_point_to_line(point, line1, line2):
    distance = np.abs((line2[1] - line1[1]) * point[0] + (line1[0] - line2[0]) * point[1] + (line2[0] - line1[0]) * line1[1] + (line1[1] -
                                                                                                                                line2[1]) * line1[0]) / np.sqrt((line2[1] - line1[1]) * (line2[1] - line1[1]) + (line1[0] - line2[0]) * (line1[0] - line2[0]))
    return int(distance)


if __name__ == '__main__':
    ori_img_dir="data/faces_from_camera/person_1_white_hat_ziying/img_face_3.png"
    
    mask_img(ori_img_dir, mask_img_dir="images/surgical.png",
             facelandmarks=facelandmarks)
    mask_img(ori_img_dir, mask_img_dir="images/cloth.png",
             facelandmarks=facelandmarks)
    mask_img(ori_img_dir, mask_img_dir="images/surgical_green.png",
             facelandmarks=facelandmarks)
    mask_img(ori_img_dir, mask_img_dir="images/N95.png",
             facelandmarks=facelandmarks)
    # mask_img(ori_img_dir="data/faces_from_camera/img_face_3.png", mask_img_dir="images/N95.png",
    #      facelandmarks=facelandmarks)
    mask_img(ori_img_dir, mask_img_dir="images/surgical_blue.png",
             facelandmarks=facelandmarks)
    mask_img(ori_img_dir, mask_img_dir="images/JHU_Mask_1.png",
             facelandmarks=facelandmarks)
    mask_img(ori_img_dir, mask_img_dir="images/JHU_Mask_2.png",
             facelandmarks=facelandmarks)
    mask_img(ori_img_dir, mask_img_dir="images/JHU_Mask_3.png",
             facelandmarks=facelandmarks)
