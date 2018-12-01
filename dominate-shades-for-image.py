#!/usr/local/bin/Python3
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

im = Image.open('test2.jpg')

color1 = im.getcolors(im.size[0]*im.size[1])
color1.sort()

def shades(n):
	n += 1 
	for i in range(1,n):
		#print(color1[-i])
		img = Image.new("RGB", (256-i*36,256-i*36), color1[-i][1])
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype("san-serif.ttf", 10)
		draw.text((0,0), "This  color  is {}".format(color1[-i][1]), (0,0,0), font=font)
		img.show()

shades(5)