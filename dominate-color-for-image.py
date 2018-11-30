#!/usr/local/bin/Python3
from PIL import Image
im = Image.open('test2.jpg')
color = max(im.getcolors(im.size[0]*im.size[1]))
img = Image.new("RGB", (256,256), color[1])
img.show()
print(color)
#img.save('color1.png')
