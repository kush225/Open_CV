import cv2												#importing python opencv
from datetime import datetime							#importing datetime for naming files w/ timestamp

def img_diff_create(x,y,z):								#defining functin for image difference
	img_diff1=cv2.absdiff(x,y)
	img_diff2=cv2.absdiff(y,z)
	img3=cv2.bitwise_and(img_diff1,img_diff2)
	return img3

threshold = 141500										#threshold for triggering "Motion Detection"
cap=cv2.VideoCapture(0) 								#starting Camera

#taking three images first
take1=cap.read()[1]
take2=cap.read()[1]
take3=cap.read()[1]

#converting them to grayscale
gray1=cv2.cvtColor(take1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(take2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(take3,cv2.COLOR_BGR2GRAY)

#lets use a time check so we only take 1 pic per sec
timecheck = datetime.now().strftime('%Ss')
while True:
		#calling function to use grayscale images
		new_img=img_diff_create(gray1,gray2,gray3)
		status,frame=cap.read()
		cv2.imshow('original',frame)						#Window showing original frame
		if cv2.countNonZero(new_img) > threshold and timecheck !=datetime.now().strftime('%Ss'):
			cv2.imwrite(datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f')+'.jpg',frame)
		timecheck =datetime.now().strftime('%Ss')
		
		#cv2.imshow('functionimg',new_img)					#Window to show changes
		
		#image transpose operation/ reading next images
		gray1=gray2
		gray2=gray3
		gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		if cv2.waitKey(30) & 0xFF == ord('q'):
			break

cv2.destroyAllWindows()
cap.release()
