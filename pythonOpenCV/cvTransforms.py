#Simple geometric transforms functions in OpenCV
#Quick demos of each which require cv2 image objects (from OpenCV_Tutorials.readImages)
#Takes imageObjs with 2+ channels. (delete chan variable for greyscale)
import cv2
import numpy as np

class switch(object):
	def __init__(self, value):
		self.value = value
		self.fall = False

	def __iter__(self):
		yield self.match
		raise StopIteration

	def match(self, *args):
		#Examine whether or not to enter a case.
		if self.fall or not args:
			return True
		elif self.value in args:
			self.fall = True
			return True
		else:
			return False

def scaling(imageObj, height, width):
	#Takes image object, scales by height factor in height and width, less than 1 shrinks etc.
	res = cv2.resize(imageObj, None, fx = height, fy = width, interpolation = cv2.INTER_CUBIC)
	return res

def translation(imageObj, x, y):
	#Translate the imageObj by x and y in thier respective directions.
	rows, cols, chan = imageObj.shape
	
	matrix = np.float32([[1, 0, x], [0, 1, y]])
	tformed = cv2.warpAffine(imageObj, matrix, (cols, rows))
	return tformed

def rotation(imageObj, angle):
	#Rotates the image by angle degrees by creating a matrix using angle as a variable.
	rows, cols, chan = imageObj.shape

	matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
	rotated = cv2.warpAffine(imageObj, matrix, (cols, rows))
	return rotated

def affineTransform(imageObj):
	#Takes and image object & two sets of coordinates.  Affine transform uses the coords as a transform 
	#matrix.
	#Points in form [[x, y], [x, y], [x, y]].
	rows, cols, chan = imageObj.shape

	pts1 = np.float32([[50,50],[200,50],[50,200]])
	pts2 = np.float32([[10,100],[200,50],[100,250]])

	matrix = cv2.getAffineTransform(pts1, pts2)
	tformed = cv2.warpAffine(imageObj, matrix, (cols, rows))
	return tformed

def perspectiveTransform(imageObj):
	#Takes three sets of coordinates and uses them to establish a new view area.  
	#Retains straight lines etc.
	rows, cols, chan = img.shape

	pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
	pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

	matrix = cv2.perspectiveTransform(pts1, pts2)
	tformed = cv2.warpPerspective(imageObj, matrix, (300, 300))
	return tformed

def morphoTransform(imageObj, type, iterations):
	kernel = np.ones((5, 5), np.uint8)

	for case in switch(type):
		if case('erosion'):
			eroded = cv2.erode(imageObj, kernel, iterations)
			return eroded
		if case('dilation'):
			dilated = cv2.dilate(imageObj, kernel, iterations)
			return dilated
		if case('opening'):
			opened = cv2.morphologyEx(imageObj, cv2.MORPH_OPEN, kernel)
			for i in range(1, iterations):
				opened = cv2.morphologyEx(opened, cv2.MORPH_OPEN, kernel)
			return opened
		if case('closing'):
			closed = cv2.morphologyEx(imageObj, cv2.MORPH_CLOSE, kernel)
			for i in range(1, iterations):
				closed = cv2.morphologyEx(closed, cv2.MORPH_CLOSE, kernel)
			return closed
		if case('gradient'):
			grad = cv2.morphologyEx(imageObj, cv2.MORPH_GRADIENT, kernel)
			for i in range(1, iterations):
				grad = cv2.morphologyEx(grad, cv2.MORPH_GRADIENT, kernel)
			return grad
		if case('tophat'):
			tipped = cv2.morphologyEx(imageObj, cv2.MORPH_TOPHAT, kernel)
			for i in range(1, iterations):
				tipped = cv2.morphologyEx(tipped, cv2.MORPH_TOPHAT, kernel)
			return tipped
		if case('blackhat'):
			bTipped = cv2.morphologyEx(imageObj, cv2.MORPH_BLACKHAT, kernel)
			for i in range(1, iterations):
				bTipped = cv2.morphologyEx(bTipped, cv2.MORPH_BLACKHAT, kernel)
			return bTipped





