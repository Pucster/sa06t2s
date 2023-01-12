import cv2
import pytesseract
import numpy as np

# from matplotlib import pyplot as plt

img = cv2.imread("i1Abv.png", cv2.IMREAD_GRAYSCALE)

ret, thresh1 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Specify structure shape and kernel size.
# Kernel size increases or decreases the area
# of the rectangle to be detected.
# A smaller value like (10, 10) will detect
# each word instead of a sentence.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 30))

# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

# Finding contours
contours, hierarchy = cv2.findContours(
    thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
)

im2 = thresh1.copy()
# labelImage = cv2.Mat(img.size(), cv2.CV_32S);

# labelImage = np.ones((img.shape),np.uint8)*255
# nLabels = cv2.connectedComponents(img, labelImage, 8);

# dst = np.ones((img.shape),np.uint8)*255
# for r in range(0,dst.shape[0]):
#     for c in range(0,dst.shape[1]):
#         label = labelImage[r, c]
#         dst[r, c] = label


cv2.imshow("Connected Components", dilation)

file = open("recognized.txt", "w+")
file.write("")
file.close()

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Drawing a rectangle on copied image
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Cropping the text block for giving input to OCR
    cropped = im2[y : y + h, x : x + w]

    file = open("recognized.txt", "a")

    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped)

    if text != "":
        file.write(text)
        file.write("\n")
        file.close

    if w > 30:
        cv2.imshow("cropped", cropped)
        # cv2.waitKey(0)

cv2.imshow("image", thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()
