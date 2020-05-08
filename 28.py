"""
http://www.pythonchallenge.com/pc/ring/bell.html

title: may pairs ring-ring

background: http://www.pythonchallenge.com/pc/ring/bell.png
(photo is of a waterfall)

"RING-RING-RING
say it out loud"
"""

from PIL import Image
import math

im = Image.open("bell.png")
px = im.load()

out = []

for i in range(0,320,2):
	for j in range(480):
		a = abs(px[i,j][1]-px[i+1,j][1])		
		if a != 42:
			out.append(a)

print(''.join([chr(x) for x in out])) # whodunnit().split()[0] ?

"""
this is a riddle about the creator of python, Guido van Rossum.

answer is guido
"""
