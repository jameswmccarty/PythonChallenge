"""
http://www.pythonchallenge.com/pc/hex/copper.html

 <!-- or maybe white.gif would be more bright-->
 http://www.pythonchallenge.com/pc/hex/white.gif

Hints: Joystick picture and the title 'emulate'

"""

from PIL import Image
from PIL import GifImagePlugin
from PIL import ImageDraw

im = Image.open("./white.gif") # looks black
#print(im.is_animated)
#print(im.n_frames)
#print(im.size)

im2 = Image.new('RGB', (200,200))
draw = ImageDraw.Draw(im2)

pos = (100,100) # center of im2
pairs = [pos]   # list of locations
"""

There is exactly one pixel in each frame of the .gif
that is not black.  It is either centered or offset 
from the center in a corner.  This represents offset
from zero and is the direction the 'joystick' points.

"""
for frame in range(im.n_frames):
	im.seek(frame)
	pxls = im.load()
	for i in range(200):
		for j in range(200):
			px = pxls[i, j]
			if px != 0:
				pos = (pos[0]+((i-100)*2),pos[1]+((j-100)*2)) # 100,100 is center frame
				pairs.append(pos)

	#if frame % 30 == 0:
	#	draw.line(tuple(pairs),fill=128,width=1)
	#	im2.show()
		
draw.line(tuple(pairs),fill=128,width=1)
im2.show() # traces out 'bonus'
