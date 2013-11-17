#!/usr/bin/python
#
#

import cv
import sys
import math
names =  ["/home/hphp/Pictures/dr_3.jpg"];

def findFirstColorPattern(img, pattern):
    """
        try to test if one pixel is in our pattern
    """
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
    cv.ShowImage("result",dest3)
    cv.WaitKey(0)
    return dest3


pattern_colors=[(255,0,0)]#(213,71,155),(67,170,228)]#red, cyan, yellow
image = cv.LoadImage(names[0])
imagesize =cv.GetSize(image)

matrix = findFirstColorPattern(image,pattern_colors)
print type(matrix)

cv.ShowImage("matrix",matrix)
'''
def xyProject(mat,imagesize):
    """
        "project" image to x and y axis
    """    
    colmask    =cv.CreateMat(imagesize[1],1,cv.CV_8UC1)
    rowmask    =cv.CreateMat(1,imagesize[0],cv.CV_8UC1)
    cv.Set(colmask,1)
    cv.Set(rowmask,1)
    colsum=[]

    for i in range(imagesize[0]):
        col = cv.GetCol(matrix,i)
        a = cv.DotProduct(colmask,col)
        colsum.append(a)
        
    rowsum =[]
    for i in range(imagesize[1]):
        row = cv.GetRow(matrix,i)
        a = cv.DotProduct(rowmask,row)
        rowsum.append(a)
        
    return (colsum,rowsum)

def getMinNonZero(arr):
    minv = max(arr)
    for a in arr:
        if a > 0 and a < minv:
            minv = a
    return minv

def getMeanDistance(data,minv):
    shiftindex = [0]
    index=[]
    
    for i in range(len(data)):
        if data[i]>minv:
            index.append(i)
            shiftindex.append(i)

    index.append(index[len(index)-1])
    dist=[]
    for i in range(len(index)):
            dist.append(index[i]-shiftindex[i])

    maxdist=max(dist)
    index=[]
    for i in dist:
        if i != maxdist and i > 1:
            index.append(i)
    mdist= sum(index)/len(index)
    #print mdist
    return mdist
if __name__ == "__main__":
    #TODO: robost against illumination change
    pattern_colors=[(219,235,102),(213,71,155),(67,170,228)]#pink, cyan, yellow
    image = cv.LoadImage(names[0])
    imagesize =cv.GetSize(image)
    
    matrix = findFirstColorPattern(image,pattern_colors)
    (colsum,rowsum) = xyProject(matrix,imagesize)

    # the following code is trying to find the edge of the small color rectangles
    rx0 = 0
    minv1 = getMinNonZero(colsum)
    for a in colsum:
        if a > minv1:
            break
        rx0 += 1
        
    minv2 = getMinNonZero(rowsum)
    ry0 = 0
    for a in rowsum:
        if a > minv2:
            break
        ry0 += 1

    arrlen = len(colsum)
    rx1 = arrlen -1 
    for i in range(arrlen):
        if colsum[arrlen-1-i] > minv1:
            break
        rx1 -= 1
        
    arrlen = len(rowsum)
    ry1 = arrlen -1 
    for i in range(arrlen):
        if rowsum[arrlen-1-i] > minv2:
            break
        ry1 -= 1

    # try to compute the mean distance between two small color rectangles
    mdist = getMeanDistance(colsum,minv1)
    rectx0 = rx0-mdist*2
    recty0 = ry0-mdist*2
    if rectx0 < 0:
        rectx0 = 0
    if recty0 < 0:
        recty0 = 0
    rectx1 = rx1+mdist*2
    if rectx1 > imagesize[0]:
        rectx1 = imagesize[0]
    recty1 = ry1+mdist*2
    if recty1 > imagesize[1]:
        recty1 = imagesize[1]

    #cv.Circle(image,(int(rx0),int(ry0)),5,cv.CV_RGB(0,255,0))
    #cv.Circle(image,(int(rx1),int(ry1)),5,cv.CV_RGB(0,255,0))
    roi = cv.GetSubRect(image,(rectx0,recty0,rectx1-rectx0,recty1-recty0))
    pt=[(rectx0,recty0),(rectx1,recty0),(rectx1,recty1),(rectx0,recty1)]
    cv.PolyLine( image, [pt], 1, cv.CV_RGB(0,255,0), 3, cv.CV_AA, 0 );
    
    cv.NamedWindow("test",cv.CV_WINDOW_AUTOSIZE)
    cv.ShowImage("test",image)
    cv.NamedWindow("roi",cv.CV_WINDOW_AUTOSIZE)
    cv.ShowImage("roi",roi)
    cv.SaveImage("result.png",image)
    cv.WaitKey(0)

    cv.DestroyWindow("test")
    cv.DestroyWindow("result")
    cv.DestroyWindow("roi")
'''
