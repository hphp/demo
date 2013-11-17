#!/usr/bin/python
#
#

import cv2
import cv
import sys
import math
import numpy
names =  ["/home/hphp/Pictures/dr_3.jpg"
,"/home/hphp/Pictures/dr.jpg"
,"/home/hphp/Pictures/dr_2.jpg"
];

def filter_color_patterns(img_src, pattern):
    pattern = 100.
    thres , dest3 = cv2.threshold(img_src,pattern,1,cv2.THRESH_BINARY)
    #ll = numpy.argwhere(dest3 == 1) #[1xxx , 2]
    #ll = numpy.argwhere(dest3 == 0) #[08xx , 2]
    #ll = numpy.argwhere(dest3 == 2) #[0000 , 2]
    dest3 = numpy.array(dest3, dtype='float32')
    print type(dest3[0][0])
    cv2.imshow("result",dest3)
    cv2.waitKey(0)
    return dest3
    """
        try to test if one pixel is in our pattern
    channels = [None, None, None]
    channels[0] = cv.CreateImage(cv.GetSize(img),8,1)#blue
    channels[1] = cv.CreateImage(cv.GetSize(img),8,1)#green
    channels[2] = cv.CreateImage(cv.GetSize(img),8,1)#red
    ch0 = cv.CreateImage(cv.GetSize(img),8,1)#blue
    ch1 = cv.CreateImage(cv.GetSize(img),8,1)#green
    ch2 = cv.CreateImage(cv.GetSize(img),8,1)#red
    cv.Split(img, ch0, ch1, ch2, None)
    dest0     = cv.CreateImage(cv.GetSize(img),8,1)
    dest1     = cv.CreateImage(cv.GetSize(img),8,1)
    dest2     = cv.CreateImage(cv.GetSize(img),8,1)
    dest3     = cv.CreateImage(cv.GetSize(img),8,1)
    cv.Smooth(ch0, channels[0], cv.CV_GAUSSIAN, 3, 3, 0)
    cv.Smooth(ch1, channels[1], cv.CV_GAUSSIAN, 3, 3, 0)
    cv.Smooth(ch2, channels[2], cv.CV_GAUSSIAN, 3, 3, 0)
    result  =[]
    for i in range(3):
        lower = pattern[i][2] - 25
        upper = pattern[i][2] + 25
        cv.InRangeS(channels[0],lower,upper,dest0)      
        lower = pattern[i][1] - 25
        upper = pattern[i][1] + 25
        cv.InRangeS(channels[1],lower,upper,dest1)
        lower = pattern[i][0] - 25
        upper = pattern[i][0] + 25        
        cv.InRangeS(channels[2],lower,upper,dest2)
        cv.And(dest0,dest1,dest3)
        temp    = cv.CreateImage(cv.GetSize(img),8,1)
        cv.And(dest2,dest3,temp)
        result.append(temp)

    cv.ShowImage("result0",result[0])
    cv.WaitKey(0)
    cv.ShowImage("result1",result[1])
    cv.WaitKey(0)
    cv.ShowImage("result2",result[2])
    cv.WaitKey(0)
    cv.Or(result[0],result[1],dest0)
    cv.Or(dest0,result[2],dest3)
    cv.NamedWindow("result",cv.CV_WINDOW_AUTOSIZE)
    """
    return dest3


for img_route in names:
    pattern_colors=[(255,0,0)]#(213,71,155),(67,170,228)]#red, cyan, yellow
    image_src = cv2.imread(img_route)
    #image_src = cv2.imread(img_route, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    #imagesize =cv.GetSize(image)

    matrix = filter_color_patterns(image_src,pattern_colors)
    print type(matrix)

#cv.ShowImage("matrix",matrix)
