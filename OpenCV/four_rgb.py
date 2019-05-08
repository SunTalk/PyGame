import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened() :

	ret, origin = cap.read()

	if ret == True :
		cv2.imshow('origin',origin)

		# b,g,r = cv2.split(origin)
		# z = np.zeros(b.shape,np.uint8)
		# red = cv2.merge((z,z,r))
		# blue = cv2.merge((b,z,z))
		# green = cv2.merge((z,g,z))

		rows,cols,channels = origin.shape
		red = origin.copy()
		green = origin.copy()
		blue = origin.copy()
		
		for i in range(rows):
			for j in range(cols):
				red[i][j][0]=0
				red[i][j][1]=0

		for i in range(rows):
			for j in range(cols):
				green[i][j][0]=0
				green[i][j][2]=0


		for i in range(rows):
			for j in range(cols):
				blue[i][j][1]=0
				blue[i][j][2]=0


		cv2.imshow('red',red)
		cv2.imshow('blue',blue)
		cv2.imshow('green',green)


		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else :
		break

cap.release()
cv2.destroyAllWindows()