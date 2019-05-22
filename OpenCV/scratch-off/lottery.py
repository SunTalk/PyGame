# Change blue color to yellow color
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
# background = cv2.imread('a.jpg')
# background = cv2.resize(background, (640, 480))

rows, columns, channels = frame.shape
mask01 = np.zeros((rows, columns), np.uint8)
yellow = np.full(frame.shape, (255, 0, 0), dtype=np.uint8)

# define range of blue color in HSV
lower_blue = np.array([110, 50, 50], dtype=np.uint8)
upper_blue = np.array([150,255,255], dtype=np.uint8)

while(1):

	# Take each frame
	ret, frame = cap.read()
	background = cv2.imread('test.jpg')
	background = cv2.resize(background, (640, 480))
	background1 = cv2.imread('bg.png')
	background1 = cv2.resize(background1, (640, 480))
	frame = cv2.flip(frame, 1)
	yellowedFrame= cv2.addWeighted(background1, 0, background, 1, 0)

	# Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	# apply a series of erosions and dilations to the mask
	# using an elliptical kernel
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
	mask = cv2.erode(mask, kernel, iterations = 2)
	mask = cv2.dilate(mask, kernel, iterations = 2)
	mask01 = cv2.bitwise_or(mask01, mask)
	mask02 = cv2.bitwise_not(mask01)
	# Bitwise-AND mask and original image
	fg = cv2.bitwise_and(background1,background1, mask= mask01)
	bg = cv2.bitwise_and(yellowedFrame, yellowedFrame, mask= mask02)
	final = cv2.add(fg, bg)
	
	cv2.imshow('final',final)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()