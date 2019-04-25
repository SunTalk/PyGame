import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while cap.isOpened() :


	ret, frame = cap.read()

	if ret == True :
		cv2.imshow('one',frame)
		frame = cv2.flip(frame,1)
		cv2.imshow('two',frame)
		frame = cv2.flip(frame,0)
		cv2.imshow('three',frame)
		frame = cv2.flip(frame,1)
		cv2.imshow('four',frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else :
		break

cap.release()
cv2.destroyAllWindows()