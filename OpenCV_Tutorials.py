import matplotlib.pyplot as plt
import PIL as Image
import cv2

#Tutorials from the Python OpenCV documentation formatted for expedited execution/learning.
#http://docs.opencv.org/trunk/doc/py_tutorials/py_tutorials.html

#Uses matplotlib, Python Imaging Library and Python OpenCV bindings 2.0.
#matplotlib displays in BGR not RGB - requires re-ordering if imported with OpenCV.

def readImages():
	#Import the images used in the tutorial functions.
	global jelly, jellyRGB, penguinBGR
	jelly = cv2.imread('images/test.jpg', 0)
	jellyRGB = cv2.imread('images/test.jpg')
	penguinRGB = cv2.imread('images/Penguins')

def imageDisplay(imageObj):
	#Display the images passed to the function.
	cv2.imshow('Image', imageObj)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def makeHists(imageObj):
	#Populate and display image histograms for Greyscale or BGR images.
	if imageObj.ndim == 2:
		#If image is greyscale, display one histogram of grey scale values:
		plt.hist(imageObj.flatten(), 256, range = (0, 250), fc = 'k')
		plt.show()
	elif imageObj.ndim == 3:
		#If image is BGR, display 3 coloured hists on top of one another:
		plt.hist(imageObj[...,0].flatten(), 256, range = (0, 250), alpha = 0.3, label = 'b')
		plt.hist(imageObj[...,1].flatten(), 256, range = (0, 250), alpha = 0.3, label = 'r')
		plt.hist(imageObj[...,2].flatten(), 256, range = (0, 250), alpha = 0.3, label = 'b')
		plt.show()

def imageAddition():
	#Merge two grayscale images using image addition
	jellyAdded = cv2.add(jelly, jelly)
	jellyAddedAgain = cv2.add(jelly, jellyAdded)
	#Create PLT window to display the added images.
	plt.subplot(131), plt.imshow(jelly, 'gray'), plt.title('Original')
	plt.subplot(132), plt.imshow(jellyAdded, 'gray'), plt.title('Added together')
	plt.subplot(133), plt.imshow(jellyAddedAgain, 'gray'), plt.title('Added three times')
	#Display:
	plt.show()

def borderPadding(imageObj):
	#Perform basic alterations to border of images.
	#Re-order for display in plt .
	r, g, b = cv2.split(imageObj)
	imageObjBGR = cv2.merge((b, g, r))
	#Perform basic alterations - creation of borders with cv2 modifiers.
	replicatedBorder = cv2.copyMakeBorder(imageObjBGR, 10, 250, 250, 10, cv2.BORDER_REPLICATE)
	reflectedBorder = cv2.copyMakeBorder(imageObjBGR, 10, 250, 250, 10, cv2.BORDER_REFLECT)
	#Create plt subplot and display the original and altered images.
	tester = plt.figure()
	tester.add_subplot(131), plt.imshow(imageObjBGR), plt.title('Original')
	tester.add_subplot(132), plt.imshow(replicatedBorder), plt.title('Replicated edge colour')
	tester.add_subplot(133), plt.imshow(reflectedBorder), plt.title('Reflected border section')
	plt.show()

def main():
	readImages()
	imageAddition()
	makeHists(jellyRGB)
	borderPadding(jellyRGB)

main()