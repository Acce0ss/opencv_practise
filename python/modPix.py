#!/usr/bin/python

import cv2
import numpy as np

img = cv2.imread('testikuvat/kisu.jpg')

#somecat = img[300:500, 330:550]
#img[200:400, 230:450] = somecat


cv2.imshow("original", cv2.resize(img, None, fx=0.5, fy=0.5))

cv2.waitKey()


b = img[:,:,0]
r = img[:,:,2]
g = img[:,:,1]

rows,cols = b.shape

blueM = np.empty((rows, cols, 3), dtype=np.uint8)
blueM[:,:] = [0,0,0]
blueM[:,:,0] = img[:,:,0] #get blue

rows,cols = g.shape

greenM = np.empty((rows, cols, 3), dtype=np.uint8)
greenM[:,:] = [0,0,0]
greenM[:,:,1] = img[:,:,1] #get blue

rows,cols = r.shape

redM = np.empty((rows, cols, 3), dtype=np.uint8)
redM[:,:] = [0,0,0]
redM[:,:,2] = img[:,:,2] #get blue
print blueM[50,200]
print img[50,200]


#cv2.imshow("blue", cv2.resize(blueM, None, fx=0.5, fy=0.5))
#cv2.imshow("green", cv2.resize(greenM, None, fx=0.5, fy=0.5))
#cv2.imshow("red", cv2.resize(redM, None, fx=0.5, fy=0.5))

#cv2.waitKey()

x = np.uint8([250])
y = np.uint8([10])

print cv2.add(x,y)
print x+y


#cv2.imshow("sum np", cv2.resize((redM+greenM), None, fx=0.5, fy=0.5))
#cv2.imshow("sum cv2", cv2.resize(cv2.add(redM,greenM), None, fx=0.5, fy=0.5))
cv2.imshow("doubled np", cv2.resize(img + img, None, fx=0.5, fy=0.5))
cv2.imshow("doubled cv2", cv2.resize(cv2.add(img,img), None, fx=0.5, fy=0.5))

cv2.waitKey()



