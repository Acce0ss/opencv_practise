#!/usr/bin/python

import cv2
import numpy as np

fgbg = cv2.BackgroundSubtractorMOG(1, 2, backgroundRatio=0.9)

count = 1
	
while (count < 6):
	frame = cv2.resize(cv2.imread('testikuvat/bgsub/frame'+str(count)+'.jpg'), None, fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
	fgmask = fgbg.apply(frame)
	cv2.imshow("Kissa!", fgmask)
	cv2.waitKey()
	count = count + 1

fgbg = cv2.BackgroundSubtractorMOG()

count = 1
	
while (count < 5):
	frame = cv2.resize(cv2.imread('testikuvat/bgsub/frame1_'+str(count)+'.jpg'), None, fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
	fgmask = fgbg.apply(frame)
	cv2.imshow("Kissa!!!", fgmask)
	cv2.waitKey()
	count = count + 1

