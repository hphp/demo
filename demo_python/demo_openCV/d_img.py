
import cv
import cv2

def cv2_img():
    img = cv2.imread('cat.5123.jpg')
    cv2.imwrite('cat.cp.jpg', img)

def cv_img():
    img = cv.LoadImage('cat.5123.jpg',0)
    cv.SaveImage('cat.cp.jpg', img)

cv_img()
