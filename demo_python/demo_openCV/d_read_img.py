
import cv2
template_img_route = "/home/hphp/Pictures/dr_3.jpg"
im_gray = cv2.imread(template_img_route, cv2.CV_LOAD_IMAGE_GRAYSCALE)
print type(im_gray),im_gray.shape
#<type 'numpy.ndarray'> (332, 500)
im_color = cv2.imread(template_img_route, cv2.CV_LOAD_IMAGE_COLOR)
print type(im_color),im_color.shape
#<type 'numpy.ndarray'> (332, 500, 3)
im_default = cv2.imread(template_img_route)
print type(im_default),im_default.shape
#<type 'numpy.ndarray'> (332, 500, 3)
im_any = cv2.imread(template_img_route, cv2.CV_LOAD_IMAGE_ANYDEPTH)
print type(im_any),im_any.shape
# no ANYDEPTH ..
