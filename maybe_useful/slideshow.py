#!/usr/bin/python

import os
import sys
import cv2
import numpy as np

dir = sys.argv[1]
time_show = int(float(sys.argv[2])*1000)
time_trans = int(float(sys.argv[3])*1000)
scale = float(sys.argv[4])
smooth_steps = 300
time_step = int(float(time_trans)/float(smooth_steps))

print time_step

all_files = os.listdir(dir)

current_img = None
next_img = None

files = []

for file in all_files:
  if ".jpg" in file:
    files.append(file)

for i, file in enumerate(files):
    print "Showing " + file
    
    current_img = cv2.resize(cv2.imread(dir+file), None, fx=scale, fy=scale)
    cv2.imshow("slideshow", current_img)
    cv2.waitKey(time_show)
    if i < (len(files)-1):
      print "next file: " + files[i+1]
      next_img = cv2.resize(cv2.imread(dir+files[i+1]), None, fx=scale, fy=scale)
      step = 0
      next_rows, next_cols, chan = next_img.shape
      curr_rows, curr_cols, chan = current_img.shape
      scaled_next = cv2.resize(next_img, (curr_cols,curr_rows))
      trans_rows = curr_rows
      trans_cols = curr_cols
      while step < smooth_steps:
        fading = (1.0/float(smooth_steps))*step
        trans_rows = curr_rows + int((next_rows-curr_rows)*(fading))
        trans_cols = curr_cols + int((next_cols-curr_cols)*(fading))
#	print "Step: " + str(step) + ", curr_rows: " +  str(curr_rows) + ", next_rows: " + str(next_rows) + ", trans_rows: " + str(trans_rows)
#	print "Step: " + str(step) + ", curr_cols: " +  str(curr_cols) + ", next_cols: " + str(next_cols) + ", trans_cols: " + str(trans_cols)
        trans_img = cv2.resize(cv2.addWeighted(current_img, (1-fading), scaled_next, fading, 0), (trans_cols,trans_rows))
#        trans_img = cv2.addWeighted(current_img, fading, cv2.resize(next_img, (curr_cols,curr_rows)), 1.0-fading, 0)
        cv2.imshow("slideshow", trans_img)
        cv2.waitKey(time_step)
        step = step + 1
        
        
