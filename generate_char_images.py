import cv2
import string
import numpy as np
import os

font = cv2.FONT_HERSHEY_PLAIN
font_prefix = "HP"
font_size = 0.8
img_size = (20, 20)
# characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
characters = string.digits
if not os.path.exists("imgpatterns"):
    os.makedirs("imgpatterns")

# Iterate over each character and generate an image
for char in characters:
    print(char)
    img = np.ones((img_size[0], img_size[1], 3), np.uint8) * 255
    text_size = cv2.getTextSize(char, font, font_size, 1)[0]
    x = (img_size[1] - text_size[0]) // 2
    y = (img_size[0] + text_size[1]) // 2
    cv2.putText(img, char, (x, y), font, font_size, (0, 0, 0), 1, cv2.LINE_AA)
    charFolder = char.lower()
    char_dir = os.path.join("imgpatterns", charFolder)
    if not os.path.exists(char_dir):
        os.makedirs(char_dir)
    if char.islower():
        prefix = "lc" + font_prefix
    elif char.isupper():
        prefix = "uc" + font_prefix
    else:
        prefix = font_prefix

    img_file = os.path.join(char_dir, prefix + char + ".png")
    print(img_file)
    cv2.imwrite(img_file, img)
