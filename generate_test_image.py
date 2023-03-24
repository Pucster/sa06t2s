import cv2
import string
import numpy as np
import os

# Define the font and font size
font = cv2.FONT_HERSHEY_TRIPLEX
font_size = 2.0

# Define the size of the image and the spacing between letters
img_width = 1800
img_height = 500
letter_spacing = int(img_width / (52 * 2))

# Create a blank white image
img = np.ones((img_height, img_width, 3), np.uint8) * 255

# Define the x-coordinate and y-coordinate of the first letter
x = letter_spacing
y = int(img_height / 4)

# Iterate over each uppercase letter and draw it on the image
for char in string.ascii_uppercase:
    # Get the size of the letter
    text_size, _ = cv2.getTextSize(char, font, font_size, 1)

    # Draw the letter on the image
    cv2.putText(img, char, (x, y), font, font_size, (0, 0, 0), 2, cv2.LINE_AA)

    # Move to the next letter's x-coordinate
    x += text_size[0] + letter_spacing

# Reset the x-coordinate to the left edge of the image
x = letter_spacing

# Move to the next row by increasing the y-coordinate
y = int(img_height * 3 / 4)

# Iterate over each lowercase letter and draw it on the image
for char in string.ascii_lowercase:
    # Get the size of the letter
    text_size, _ = cv2.getTextSize(char, font, font_size, 1)

    # Draw the letter on the image
    cv2.putText(img, char, (x, y), font, font_size, (0, 0, 0), 2, cv2.LINE_AA)

    # Move to the next letter's x-coordinate
    x += text_size[0] + letter_spacing

# Display the image
cv2.imshow("Letters", img)
cv2.waitKey(0)
img_file = os.path.join("./" + "testimageHT.png")
cv2.imwrite(img_file, img)
cv2.destroyAllWindows()
