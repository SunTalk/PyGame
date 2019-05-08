import numpy as np
import cv2

def InsertLogo(img1, img2, x, y):
	# I want to put logo on top-left corner, So I create a ROI
	rows,cols,channels = img2.shape
	roi = img1[x:x+rows, y:y+cols ]
	# Now create a mask of logo and create its inverse mask also
	img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
	mask_inv = cv2.bitwise_not(mask)
	# Now black-out the area of logo in ROI
	img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
	# Take only region of logo from logo image.
	img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
	# Put logo in ROI and modify the main image
	dst = cv2.add(img1_bg,img2_fg)
	img1[x:x+rows, y:y+cols ] = dst
	return img1

	
def InsertLogo_2(img1, img2, x, y):
	# Direct access pixels of images to put logo
	rows,cols,channels = img2.shape
	roi = img1[x:x+rows, y:y+cols ]
	# Now create a mask of logo and create its inverse mask also
	img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
	for i in range(rows):
		for j in range(cols):
			if mask[i][j] != 0:
				img1[i+x][j+y]=img2[i][j]
	return img1

cap = cv2.VideoCapture(0)
img = cv2.imread('bg.png')
img = cv2.resize(img,(640,480))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray,0, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

slime = cv2.imread('slime.png')
slime = cv2.resize(slime,(200,100))
rowsLogo,colsLogo,channelsLogo = slime.shape
x = 50
y = 220

while cap.isOpened() :


	ret, frame = cap.read()

	if ret == True :
		frame=cv2.resize(frame,(640,480))
		frame=cv2.flip(frame,1)

		rowsFrame,colsFrame,channelsFrame = frame.shape
		InsertLogo_2(frame, slime, x, y)

		roi=frame[:]
		roi=cv2.bitwise_and(roi,roi,mask = mask_inv)
		img=cv2.bitwise_and(img,img,mask = mask)
		dst = cv2.add(roi,img)
		cv2.imshow('PIC', dst)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else :
		break

cap.release()
cv2.destroyAllWindows()