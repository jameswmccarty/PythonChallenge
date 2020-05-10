"""
http://www.pythonchallenge.com/pc/ring/grandpa.html

title: Where am I?
photo: http://www.pythonchallenge.com/pc/ring/grandpa.jpg
(shows a rock on a lake)

Next link: http://www.pythonchallenge.com/pc/rock/grandpa.html
username: island
password: country

Searching for 'Grandfather's Rock'
http://www.kosamui.com/lamai-beach/hinta-hinyai.htm

Island is kohsamui
Country is thailand

<!-- short break, this ***REALLY*** has nothing to do with Python -->

http://www.pythonchallenge.com/pc/rock/grandpa.html

"That was too easy, you are still on 31..."

Title: UFOs

<img src="mandelbrot.gif" border="0">
	<window left="0.34" top="0.57" width="0.036" height="0.027"/>
	<option iterations="128"/>

"""

from PIL import Image
from PIL import ImageOps

def calcpoint(x, y, imax):
	i = 0
	x0 = x
	y0 = y
	while x*x + y*y <= 4. and i < imax:
		t = x*x - y*y + x0
		y = 2.*x*y + y0
		x = t	       
		i += 1
	return i


xres = 640
yres = 480
xmin   = 0.34
width  = 0.036
ymin   = 0.57
height = 0.027
#im   = Image.new('RGB', (640,480))
im   = Image.new('L', (640,480))
#pal  = img.getpalette()
sp   = im.load()
for x in range(xres):
	for y in range(yres):
		x0 = xmin + x/xres*(width)
		y0 = ymin + y/yres*(height) 	
		z = calcpoint(x0, y0, 127)
		#sp[x,y] = (pal[z*3],pal[z*3+1],pal[z*3+2])
		sp[x,y]  = z
		
im = ImageOps.flip(im)
#im.show()

img = Image.open("mandelbrot.gif")
px  = img.load()
#img.show()

diffs = []
mine = im.getdata()
orig = img.getdata()
for i in range(len(mine)):
	if mine[i] != orig[i]:
		diffs.append(orig[i] - mine[i])
print(len(diffs))
print(diffs)
out = Image.new('L', (23,73))
op = out.load()
for i in range(23):
	for j in range(73):
		op[i,j] = 0 if diffs[j*23+i] < 0 else 255
out.show() # https://en.wikipedia.org/wiki/Arecibo_message

