import os
import cv2
import pytesseract
from translate import Translator
import string
import time

directory = "./images"


def img_to_string(filename):
    os.system("say new file found %s" % file_name)
    # reading file to an img object
    img = cv2.imread(os.path.join(directory, filename), 0)
    # getting text from the image object using the Tesseract library
    text_map[filename] = pytesseract.image_to_string(img)
    if (text_map[file_name]) == "":
        print("no text found in %s" % file_name)
        os.system("say no text found in %s" % file_name)
        return
    # output the text to the console
    print("Text found in file: " + filename)
    print("---------------------------")
    print(".%s." % text_map[file_name])
    # text2speech using MacOS 'say' system function
    os.system(
        "say -v Daniel %s"
        % text_map[file_name]
        .replace("\n", " ")
        .replace("\r", "")
        .translate(str.maketrans("", "", string.punctuation))
    )


def translate(filename, text):
    if (text) == "":
        os.system("say no text to translate in %s" % file_name)
        print("no text to translate in %s" % file_name)
        return
    os.system("say Attempting to translate to Romanian")
    # creating the translator object
    translator = Translator(from_lang=language, to_lang="ro")
    # translating the text to Romanian
    translated_text = translator.translate(text)
    # adding the translated text to the map
    translated_text_map[filename] = translated_text
    # output the translated text to the console
    print("Translation to Romanian: ")
    print("---------------------------")
    print(".%s." % translated_text_map[filename])
    # text2speech using MacOS 'say' system function
    os.system(
        "say -v Ioana %s"
        % translated_text_map[filename]
        .replace("\n", " ")
        .replace("\r", "")
        .translate(str.maketrans("", "", string.punctuation))
    )


text_map = {}
translated_text_map = {}
language = "fr"

os.system("say Starting text recognition for files in %s " % directory)

while True:
    for file_name in os.listdir(directory):
        if (
            os.path.splitext(file_name)[1]
            in (
                ".jpg",
                ".png",
                ".jpeg",
                ".bmp",
                ".gif",
                ".webp",
            )
            and file_name not in text_map.keys()
        ):
            img_to_string(file_name)
            translate(file_name, text_map[file_name])
    time.sleep(10)
