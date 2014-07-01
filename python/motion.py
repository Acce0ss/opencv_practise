#!/usr/bin/python

import cv2
import numpy as np

fgbg = cv2.BackgroundSubtractorMOG(10, 1, 0.5, 0)

capt = cv2.VideoCapture('testikuvat/test2.mp4')

ret, otos = capt.read()
first = cv2.cvtColor(cv2.resize(otos, None, fx=0.25, fy=0.25), cv2.COLOR_BGR2HSV)

if capt:
	while True:
		ret, otos = capt.read()
		frame = cv2.resize(otos, None, fx=0.25, fy=0.25)
		fgmask = fgbg.apply(frame)

		rows,cols = fgmask.shape

		mask = np.empty((rows,cols, 3), dtype=np.uint8)
		mask[:,:,0] = fgmask
		mask[:,:,1] = fgmask
		mask[:,:,2] = fgmask

		kernel = np.ones((5,5),np.uint8)
		test = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
		cv2.imshow("Track", cv2.bitwise_and(mask, frame))
		cv2.imshow("Track2", test)
		cv2.imshow("vid", frame)
		cv2.imshow("diff", cv2.absdiff(frame, first))
		

		key = cv2.waitKey(10)
		if key == ord('q'):
                	break
cv2.destroyAllWindows()
