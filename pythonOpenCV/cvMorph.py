#A selection of morphological function demos

import cv2
import numpy as np

def erosion(imageObj, iterations):
	kernel = np.ones((5, 5), np.uint8)
	eroded = cv2.erode(img, kernel, iterations)
	return eroded