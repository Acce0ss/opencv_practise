#!/usr/bin/python

import cv2
import numpy as np

fgbg = cv2.BackgroundSubtractorMOG(500, 50, 0.5, 0)

#capt = cv2.VideoCapture('cars.mp4')
capt = cv2.VideoCapture('test.avi')

scale = 0.5

ret, otos = capt.read()
first = otos

if capt:
	while True:
		ret, otos = capt.read()
		frame = otos
		proc_frame = cv2.equalizeHist(cv2.cvtColor(otos, cv2.COLOR_BGR2GRAY))
		proc_frame = cv2.medianBlur(proc_frame, ksize=15)

		fgmask = fgbg.apply(proc_frame)

		rows,cols = fgmask.shape

		ret, diff = cv2.threshold(cv2.cvtColor(cv2.absdiff(frame, first), cv2.COLOR_BGR2GRAY), 40, 255, cv2.THRESH_BINARY)

		kernel = np.ones((11,11),np.uint8)
		diff2 = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
		kernel = np.ones((11,11),np.uint8)
		diff2 = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)

		contours,hierarchy = cv2.findContours(diff2.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#		print contours
#		contours = []
		
		cnt = []
		M = []
		box = None
		x = y = w = h = None
		if contours:
		  cnts = contours[0]
		  cnt = cv2.convexHull(cnts)
		  M = cv2.moments(cnt)
		  x,y,w,h = cv2.boundingRect(cnt)
		  cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
		  rect = cv2.minAreaRect(cnt)
		  box = cv2.cv.BoxPoints(rect)
		  box = np.int0(np.around(box))
		  cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

		cv2.imshow("Track", cv2.resize(fgmask, None, fx=scale, fy=scale))
		cv2.imshow("Frame", cv2.resize(frame, None, fx=scale, fy=scale))
		cv2.imshow("Diff", cv2.resize(diff, None, fx=scale, fy=scale))
		cv2.imshow("Diff2", cv2.resize(diff2, None, fx=scale, fy=scale))
		key = cv2.waitKey(10)
		if key == ord('q'):
                	break
cv2.destroyAllWindows()
