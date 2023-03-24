import cv2
import numpy as np

patterns = {}

# Iterate through each training image
for i in range(1):
    # Load the image
    img = cv2.imread("meta.jpg")
    # Preprocess the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    thresh = cv2.erode(thresh, kernel, iterations=1)
    thresh = cv2.dilate(thresh, kernel, iterations=2)
    # Extract the text region and its pattern
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = float(w) / h
    if aspect_ratio > 1 and cv2.contourArea(contour) > 100:
        text_region = img[y : y + h, x : x + w]
        pattern = []
        for i in range(h):
            for j in range(w):
                if text_region[i, j, 0] < 128:
                    pattern.append((i, j))
        label = get_label_from_filename("image{}.jpg".format(i))
        if label in patterns:
            patterns[label].append(pattern)
        else:
            patterns[label] = [pattern]

from sklearn.decomposition import PCA

# Concatenate all the patterns into a single array
X = np.concatenate([np.array(patterns[label]) for label in labels])

# Fit PCA on the patterns
pca = PCA(n_components=10)
pca.fit(X)

# Reduce the dimensionality of each pattern using PCA
for label in labels:
    patterns[label] = pca.transform(patterns[label])
