
from PIL import Image
import pylab
import numpy

img = Image.open(open("cat.5123.jpg"))
print img.size
nimg = numpy.asarray(img, dtype='int32')
print nimg.shape
pylab.imshow(img)
pylab.show()
cropped = img.crop((0,0,400,374))
pylab.imshow(cropped)
pylab.show()
cropped.save("part_cat.jpg")
