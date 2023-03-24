import cv2, os, json, string
from mylib import print_pattern

source_images_dir = "imgpatterns/"
characters = {}
patterns = {}
img_size = (20, 20)

for char in string.ascii_lowercase + string.digits:
    char_folder = os.path.join(source_images_dir, str(char))
    char_files = os.listdir(char_folder)
    char_images = [
        cv2.imread(os.path.join(char_folder, f), cv2.IMREAD_GRAYSCALE)
        for f in char_files
        if not f.startswith(".")
    ]
    characters[str(char)] = char_images
    # resize all and threshold
    for i, img in enumerate(characters[str(char)]):
        img = cv2.resize(img, img_size)
        _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        characters[str(char)][i] = img

    char_patterns = []
    for _, img in enumerate(characters[str(char)]):
        pattern = []
        for j, pixel in enumerate(img.flatten()):
            if pixel > 128:
                x = j % img_size[1]
                y = j // img_size[1]
                pattern.append((x, y))
        char_patterns.append(pattern)
        print_pattern(pattern)
    patterns[char] = char_patterns


with open("patterns.json", "w") as f:
    json.dump(patterns, f)
