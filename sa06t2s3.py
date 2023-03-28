import cv2, json, string, os, random, time
import numpy as np
import mylib as ml

with open("patterns.json", "r") as f:
    patterns = json.load(f)
sourcefile = "images/black-and-white-text-true-Favim.com-419872.jpg"

text_region_save_results = {}
acc_list = []

# load image in grayscale
img = cv2.imread(sourcefile, cv2.IMREAD_GRAYSCALE)
# also keep a copy of it in RGB
imgc = cv2.imread(sourcefile, cv2.COLOR_BGR2RGB)
print(max(img.shape) / 10)

# Compute the horizontal and vertical Sobel gradients
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
# Compute the gradient magnitude and direction
grad_mag = np.sqrt(sobelx**2 + sobely**2)
grad_dir = np.arctan2(sobely, sobelx)
# Threshold the gradient magnitude
thresh_value = 128
binary_img = np.zeros_like(grad_mag)
binary_img[grad_mag > thresh_value] = 255
# Threshold the image
thresh_value = 128
binary_img = np.zeros_like(img)
binary_img[img > thresh_value] = 255
# Find contours in the binary image
contours, hierarchy = cv2.findContours(
    binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)

# iterate through contours and look for characters
# this will eventually result in some areas containing stuff
# those areas will be resized to match the pattern size
# then a method from the previous century will be used to check for matches
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    # for i in range(len(contours)):
    #     if hierarchy[0, i, 3] == -1:
    #         # This contour has no parent, so it is not inside any other contour
    #         x, y, w, h = cv2.boundingRect(contours[i])
    #         contour = contours[i]
    # just look at contours that might make sense - small ones can be ignored
    if cv2.contourArea(contour) > max(img.shape) / 12:
        text_region = img[y : y + h, x : x + w]
        black = 0
        for i in range(h):
            for j in range(w):
                if img[y + i, x + j] > 128:
                    black += 1
        # this is an attempt to skip 'holes'. For some reason I can't figure out how to not look at them
        if black / (h * w) > 0.8:
            print("Skipping contour as it is too white!")
            continue
        # Resize the text region to 20x20 so it has the same dimensions as the patterns
        text_region = cv2.resize(text_region, (20, 20))
        thresh_value = 128
        txt_bin_img = np.zeros_like(text_region)
        txt_bin_img[text_region > thresh_value] = 255
        _, text_region = cv2.threshold(
            text_region, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        _, text_region = cv2.threshold(
            text_region, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        pattern = []
        full = 1
        for i in range(20):
            for j in range(20):
                if text_region[i, j] == 0:
                    pattern.append([j, i])
                    full -= 1 / 400
        # this should get rid of dots and dashes and stuff but it doesn't really
        # if full > 0.9:
        #     print("Too full!")
        #     continue

        # don't look at contours that are mostly empty - also attempting to get rid of 'holes'
        if full > 0.2:
            start = time.time()
            match, character = ml.recognize_pattern(pattern, patterns)
            elapsed = time.time() - start
            message = "Matched {char} with {acc:.2f}% accuracy in {elapsed:.2f}s"
            print(message.format(char=character, acc=match * 100, elapsed=elapsed))
            acc_list.append(match)
            random_string = "".join(
                random.choices(string.ascii_lowercase + string.digits, k=16)
            )
            text_region_save_results[random_string] = [txt_bin_img, character, match]
        else:
            continue
        if character == None:  # doesn't happen anymore but I left this test here :D
            character = "?"
        cv2.rectangle(imgc, (x, y), (x + w, y + h), (0, 200, 0), 1)
        cv2.putText(
            imgc,
            character.upper(),
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            1,
            cv2.LINE_AA,
        )
message = "{chars} - avg(acc): {acc:.2f}%"
accuracy = sum(acc_list) / len(acc_list) * 100
print(message.format(chars=len(acc_list), acc=accuracy))
cv2.putText(
    imgc,
    message.format(chars=len(acc_list), acc=accuracy),
    (10, imgc.shape[0] - 10),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.5,
    (0, 0, 255),
    1,
    cv2.LINE_AA,
)

# the "learning" phase will iterate through all findings and ask the user to validate the matches
# pressing Esc will just skip the image
# pressing the character will save the current image as a pattern for that character
# I add a pattern if a mismatch happens or no mismatch but accuracy is too low
# after the learning phase you have to re-run the pattern generation script
print("Press 'l' to enter the learning phase, any other key to exit")
cv2.imshow("Text Regions", imgc)
learn = cv2.waitKey(0)
cv2.destroyAllWindows()
random_string = "".join(random.choices(string.ascii_lowercase + string.digits, k=16))
cv2.imwrite("results/" + random_string + ".png", imgc)

message = "This image was identified as '{char}' with {acc:.2f}% accuracy . Press Esc to ignore, press the correspondent character to add a pattern to the pattern library."
if chr(learn) == "l":
    for key in text_region_save_results.keys():
        thisImage = text_region_save_results[key][0]
        char = text_region_save_results[key][1]
        score = text_region_save_results[key][2]
        if score < 1:
            print(message.format(char=char, acc=score * 100))
            cv2.imshow("Learn", thisImage)
            cv2.resizeWindow("Learn", 100, 100)
            key_pressed = cv2.waitKey(0)
            if key_pressed == 27:
                continue
            else:
                output_file = os.path.join(
                    "./imgpatterns/"
                    + chr(key_pressed)
                    + "/"
                    + key
                    + "_"
                    + chr(key_pressed)
                    + ".png"
                )
                print("Writing new image pattern to " + output_file)
                if not cv2.imwrite(output_file, thisImage):
                    print("Cannot save image!")
            cv2.destroyAllWindows()
    print("Run 'generate_patterns_from_images.py' to update the pattern library now!")
print("OK then, bye!")

cv2.destroyAllWindows()
