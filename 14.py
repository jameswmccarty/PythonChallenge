"""
http://www.pythonchallenge.com/pc/return/italy.html
"""
from PIL import Image
im = Image.open("wire.png")
px = im.load()

sp = Image.new('RGB', (100,100))
sppx = sp.load()

#for idx in range(100*100):
	#sppx[idx%100,idx//100] = px[idx,0] # bit -> wrong curve

# wire is a 100*100 pixel long image
# it wraps 'around' in a spiral from the outside in
# there is a square perimeter p, and an offset b
# to go around 1 time (starting from 100)
# it is 100 steps (top), 99 steps (right side), 99 steps
# (bottom), and 98 steps (left).
# The next number of steps to take across the top
# will be 98.  The offset goes up by one.

p = 100
b = 0
idx = 0
while idx < 100*100:
	for x in range(p):
		sppx[b+x,b] = px[idx,0]
		idx += 1
	for x in range(p-1):
		sppx[p-1+b,x+1+b] = px[idx,0]
		idx += 1
	for x in range(p-1):
		sppx[p-2-x+b,p-1+b] = px[idx,0]
		idx += 1
	for x in range(p-2):
		sppx[b,p-2-x+b] = px[idx,0]
		idx += 1
	p -= 2
	b += 1
sp.show() # shows a cat -> uzi
		


		
