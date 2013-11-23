#!/bin/python
from PIL import Image 

# generate a blank picture , and draw a line
im = Image.new('RGB', (460, 510), 0xffffff)
draw = ImageDraw.Draw(im)
width,height = im.size
# draw a line , with 30 pixal each line , first line with 40pixal
for i in range(1,17):
    y=i*30+10;
    draw.line(((10, y),(width-10,y)) , fill=(225,225,225))
#board
draw.line(((10, 1),(10,height-20)) , fill=(225,225,225))
draw.line(((width-10, 1),(width-10,height-20)) , fill=(225,225,225))
