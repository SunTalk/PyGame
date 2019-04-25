import numpy as np
import cv2

def nothing(x):
	pass

cap = cv2.VideoCapture(1)

# cv2.namedWindow('BW')
# cv2.createTrackbar('Trackbar1', 'BW', 100, 255, nothing)

# cv2.namedWindow('Edge')
# cv2.createTrackbar('Trackbar2', 'Edge', 100, 255, nothing)
# cv2.createTrackbar('Trackbar3', 'Edge', 200, 255, nothing)

while cap.isOpened() :

	ret, frame = cap.read()

	if ret == True :
		cv2.imshow('one',frame)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.flip(gray,1)
		cv2.imshow('two',gray)
		# thrs1 = cv2.getTrackbarPos('Trackbar1', 'BW')
		ret, balck_and_white= cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
		balck_and_white = cv2.flip(balck_and_white,0)
		cv2.imshow('three',balck_and_white)

		# thrs2 = cv2.getTrackbarPos('Trackbar2', 'Edge')
		# thrs3 = cv2.getTrackbarPos('Trackbar3', 'Edge')
		gray = cv2.flip(gray,0)
		gray = cv2.flip(gray,1)
		edge = cv2.Canny(gray,80,80)
		cv2.imshow('four', edge)


		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else :
		break

cap.release()
cv2.destroyAllWindows()