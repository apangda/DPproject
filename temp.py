# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2 
 
cap = cv2.VideoCapture('WIN_20201207_16_43_03_Pro.mp4') 
 
while(cap.isOpened()): 
    ret, frame = cap.read() 
    cv2.imshow('image', frame) 
    k = cv2.waitKey(0) 
    #q键退出
    if (k & 0xff == ord('q')): 
        break
 
cap.release() 
cv2.destroyAllWindows()




