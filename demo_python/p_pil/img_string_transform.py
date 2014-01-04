import StringIO
from PIL import Image

image = Image.open("cp.jpg")
output = StringIO.StringIO()
#image.save("good.jpg")
image.save(output, format='JPEG')
contents = output.getvalue()
print type(contents)
print contents
output.close()
