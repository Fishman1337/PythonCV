#A selection of feature detection & description demos

import cv2
import numpy as np 

def harrisCorner(imageObj):
	#Simple harris corner detection.
	#Creates a grayscale version of the imageObj
	gray = cv2.cvtColor(imageObj, cv2.COLOR_BGR2GRAY)
	
	npgray = np.float32(gray)
	dst = cv2.cornerHarris(npgray, 2, 3, 0.04)

	dst = cv2.dilate(dst, None)

	imageObj[dst > 0.01 * dst.max()] = [0, 0, 255]

	return imageObj

def harrisRefined(imageObj):
	#Runs harris as above, then looks for sub-pixels within the discovered corners.
	gray = cv2.cvtColor(imageObj, cv2.COLOR_BGR2GRAY)
	gray = npfloat32()

	return 0

def siftMatching(imageObj, secondObj):
	sift = cv2.SIFT()
	kp1, des1 = sift.detectAndCompute(imageObj, None)
	kp2, des2 = sift.detectAndCompute(secondObj, None)

	FLANN_INDEX_KDTREE = 0
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
	search_params = dict(checks = 50)

	flann = cv2.FlannBasedMatcher(index_params, search_params)

	matches = flann.knnMatch(des1, des2, k = 2)

	matchesMask = [[0, 0] for i in xrange(len(matches))]

	for i, (m, n) in enumerate(matches):
		if m.distance < 0.7 * n.distance:
			matchesMask[i] = [1, 0]

	draw_params = dict(matchColor = (0, 255, 0),
					   singlePointColor = (255, 0, 0),
					   matchesMask = matchesMask,
					   flags = 0)

	matched = cv2.drawMatches(imageObj, kp1, secondObj, kp2, matches, None, **draw_params)

	return matched



