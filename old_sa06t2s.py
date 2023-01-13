import os
import cv2
import pytesseract
from translate import Translator
import string

# directory containing images
directory = "./"

text_map = {}
translated_text_map = {}
language = "fr"

# iterate through all files in directory
for filename in os.listdir(directory):
    # check if file is an image
    if os.path.splitext(filename)[1] in (
        ".jpg",
        ".png",
        ".jpeg",
        ".bmp",
        ".gif",
        ".webp",
    ):
        # read image
        img = cv2.imread(os.path.join(directory, filename))

        # get text
        text = pytesseract.image_to_string(img, lang="fra")
        text_map[filename] = text

        # translate text from English to Romanian
        translator = Translator(from_lang=language, to_lang="ro")
        translated_text = translator.translate(text)

        # add translated text to dictionary with filename as key
        translated_text_map[filename] = translated_text

for key in text_map:
    print("Text found in file: " + key)
    print("---------------------------")
    print(text_map[key])
    os.system(
        "say -v Daniel %s"
        % text_map[key]
        .replace("\n", " ")
        .replace("\r", "")
        .translate(str.maketrans("", "", string.punctuation))
    )
    print("---------------------------")
    print("Translation to Romanian: ")
    print("---------------------------")
    print(translated_text_map[key])
    os.system(
        "say -v Ioana %s"
        % translated_text_map[key]
        .replace("\n", " ")
        .replace("\r", "")
        .translate(str.maketrans("", "", string.punctuation))
    )
    print("============================")
