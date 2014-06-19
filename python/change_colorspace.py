#!/usr/bin/python

import cv2
import numpy as np

img = cv2.imread('testikuvat/kisu.jpg')

cv2.imshow("Kissa!", img)

cv2.waitKey()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

green = np.uint8([[[0, 255, 0]]])
print cv2.cvtColor(green, cv2.COLOR_BGR2HSV)

lower_blue = np.array([20,50,50])
upper_blue = np.array([60,255,255])

mask = cv2.inRange(gray, lower_blue, upper_blue)

res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Kissa!", res)

cv2.waitKey()
