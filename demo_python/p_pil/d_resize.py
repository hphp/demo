from PIL import Image


image = Image.open("cp.jpg")
img = image.resize((100,100))
img.show()
