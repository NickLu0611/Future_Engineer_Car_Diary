# Python code for Multiple Color Detection 

import numpy as np 
import cv2
import pickle
import time


# Capturing video through webcam 
webcam = cv2.VideoCapture(0)


def undistort(img, cal_dir='image/cal_pickle.p'): 

    with open(cal_dir, mode='rb') as f: 

        file = pickle.load(f) 

    mtx = file['mtx'] 

    dist = file['dist'] 

    dst = cv2.undistort(img, mtx, dist, None, mtx) 

    return dst

# Start a while loop 
while(1): 
	# Reading the video from the 
	# webcam in image frames
	success, img = webcam.read()
	imageFrame = img

	# Convert the imageFrame in 
	# BGR(RGB color space) to 
	# HSV(hue-saturation-value) 
	# color space 
	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 

	# Set range for red color and 
	# define mask 
	red_lower = np.array([0, 50, 100], np.uint8) 
	red_upper = np.array([5, 255, 255], np.uint8)
	red_lower2 = np.array([160, 50, 100], np.uint8) 
	red_upper2 = np.array([180, 255, 255], np.uint8) 
	red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
	red_mask2 = cv2.inRange(hsvFrame, red_lower2, red_upper2)
	red_mask = red_mask | red_mask2

	# Set range for green color and 
	# define mask 
	green_lower = np.array([50, 100, 85], np.uint8) 
	green_upper = np.array([75, 255, 255], np.uint8) 
	green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 
	
	# Morphological Transform, Dilation 
	# for each color and bitwise_and operator 
	# between imageFrame and mask determines 
	# to detect only that particular color 
	kernal = np.ones((5, 5), "uint8") 
	
	# For red color 
	red_mask = cv2.dilate(red_mask, kernal) 
	res_red = cv2.bitwise_and(imageFrame, imageFrame, 
							mask = red_mask) 
	
	# For green color 
	green_mask = cv2.dilate(green_mask, kernal) 
	res_green = cv2.bitwise_and(imageFrame, imageFrame, 
								mask = green_mask) 

	# Creating contour to track red color 
	contours, hierarchy = cv2.findContours(red_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE) 
	
	for pic, contour in enumerate(contours): 
		area = cv2.contourArea(contour) 
		if(area > 500): 
			x, y, w, h = cv2.boundingRect(contour) 
			imageFrame = cv2.rectangle(imageFrame, (x, y), 
									(x + w, y + h), 
									(0, 0, 255), 2) 
			
			cv2.putText(imageFrame, "Red Colour", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 1.0, 
						(0, 0, 255))

	# Creating contour to track green color 
	contours, hierarchy = cv2.findContours(green_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE) 
	
	for pic, contour in enumerate(contours): 
		area = cv2.contourArea(contour) 
		if(area > 300): 
			x, y, w, h = cv2.boundingRect(contour) 
			imageFrame = cv2.rectangle(imageFrame, (x, y), 
									(x + w, y + h), 
									(0, 255, 0), 2) 
			
			cv2.putText(imageFrame, "Green Colour", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 
						1.0, (0, 255, 0))
			# Program Termination
	cv2.imshow("Multiple Color Detection in Real-Time", imageFrame)	
	if cv2.waitKey(10) & 0xFF == ord('q'): 
		webcam.release() 
		cv2.destroyAllWindows() 
		break