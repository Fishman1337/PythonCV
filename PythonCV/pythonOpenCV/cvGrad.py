import cv2
import numpy as np 
from matplotlib import pyplot as plt 

def imageGradient(imageObj):
	laplacian = cv2.Laplacian(imageObj, cv2.CV_64F)
	sobelX = cv2.Sobel(imageObj, cv2.CV_64f, 1, 0, ksize = 5)
	sobelY = cv2.Sobel(imageObj, cv2.CV_64F, 0, 1, ksize = 5)

	plt.subplot(2, 2, 1), plt.imshow(imageObj, cmap = "gray")
	plt.title("Original"), plt.xticks([]), plt.yticks([])
	plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap = "gray")
	plt.title("Laplacian"), plt.xticks([]), plt.yticks([])
	plt.subplot(2, 2, 3), plt.imshow(sobelX, cmap = "gray")
	plt.title("Sobel X"), plt.xticks([]),  plt.yticks([])
	plt.subplot(2, 2, 4), plt.imshow(sobelY, cmap = "gray")
	plt.title("Sobel Y"), plt.xticks([]), plt.yticks([])

	plt.show()