#!/usr/bin/python

import cv2
import numpy as np

img = cv2.imread('testikuvat/persp.jpg')

pts1 = np.float32([[428,1068],[1426,1102],[298, 1788],[1606,1794]])
pts2 = np.float32([[0,0],[1000,0],[0,600],[1000,600]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img, M, (1000,600))

cv2.imshow("original", cv2.resize(img, None, fx=0.25, fy=0.25))
cv2.imshow("result", dst)

cv2.waitKey()
