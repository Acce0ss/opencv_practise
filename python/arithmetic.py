#!/usr/bin/python

import cv2
import numpy as np

img = cv2.imread('testikuvat/kisu.jpg')

#somecat = img[300:500, 330:550]
#img[200:400, 230:450] = somecat


cv2.imshow("original", cv2.resize(img, None, fx=0.5, fy=0.5))

cv2.waitKey()

cv2.imshow("doubled np", cv2.resize(img + img, None, fx=0.5, fy=0.5))
cv2.imshow("doubled cv2", cv2.resize(cv2.add(img,img), None, fx=0.5, fy=0.5))

cv2.waitKey()

height,width = img.shape[:2]
print [width, height]
sun = cv2.resize(cv2.imread('testikuvat/sunshine.jpg'), (width, height))

print sun.shape

shiny = cv2.addWeighted(img,0.8,cv2.add(sun, sun),0.2,0)

cv2.imshow("shiny cat", cv2.resize(cv2.add(shiny, (0.25*shiny).astype(np.uint8)), None, fx=0.5, fy=0.5))

cv2.waitKey()
