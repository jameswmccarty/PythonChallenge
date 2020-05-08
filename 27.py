"""
http://www.pythonchallenge.com/pc/hex/speedboat.html

title: between the tables

<!-- oh, and this is NOT a repeat of 14 -->

(Puzzle 14 was the spiral)

<img src="zigzag.jpg"> <!-- did you say gif? -->

Links to: http://www.pythonchallenge.com/pc/ring/bell.html
Requires next username/password

"""

from PIL import Image
from PIL import GifImagePlugin
import bz2
import keyword

im = Image.open("zigzag.gif")
px = im.load()
col_map = im.getpalette()[::3]

# replace every pixel value with the value
# at it's index in the palette data
sp = Image.new('L', (320,270))
sppx = sp.load()
for i in range(320):
	for j in range(270):
		sppx[i, j] = col_map[px[i, j]]

# determine differing pixels (offset by one)
newbytes = b'\xFF'
diffbytes = b''
for idx in range(320*270-1):
	if im.tobytes()[idx+1] == sp.tobytes()[idx]:
		newbytes += b'\xFF'
	else:
		newbytes += b'\x00'
		diffbytes += bytes([im.tobytes()[idx+1]])
sp2 = Image.frombytes('L',(320,270),newbytes)
#sp2.show() # not key word | busy?

solved = set([x for x in str(bz2.decompress(diffbytes)).split(' ') if x not in keyword.kwlist])

print(solved) #{"b'../ring/bell.html", 'exec', 'repeat', 'print', "while'", '../ring/bell.html', 'switch'}

# username: repeat
# password: switch
