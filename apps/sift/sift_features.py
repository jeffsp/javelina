#!/usr/bin/python

# @file sift_features.py
# @brief SIFT feature detector
# @author Jeff Perry <jeffsp@gmail.com>
# @version 1.0
# @date 2014-09-19

import sys
import cv2
import numpy as np

usage="sift_features.py <input.jpg>"

def get_keypoints(img):

    # convert to grayscale
    g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # get the keypoints
    #sift = cv2.SIFT(contrastThreshold=0.05)
    #sift = cv2.SIFT(nfeatures=3000)
    sift = cv2.SIFT()
    kp=sift.detect(g,None)

    return kp

if __name__ == '__main__':

    # check args
    if len(sys.argv)!=2:
        print "usage",usage
        sys.exit(-1)

    # read it
    img=cv2.imread(sys.argv[1])

    # get them
    kp=get_keypoints(img)

    # print them
    print len(kp)," keypoints detected"
    for i in kp:
        print i.pt,i.size,i.angle,i.response,i.octave,i.class_id

    # Draw them
    img=cv2.drawKeypoints(img,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("SIFT keypoints",img)
    cv2.waitKey(0)
