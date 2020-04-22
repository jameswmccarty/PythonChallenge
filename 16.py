"""
http://www.pythonchallenge.com/pc/return/mozart.html
"""

from PIL import Image
im = Image.open("mozart.gif")
im = im.convert('RGB')
px = im.load()

marker = (255,0,255) # magenta

def find_colidx(row):
	idx = 0
	marked = False
	while not marked:
		marked = True
		for j in range(5):			
			if px[idx+j,row] != marker:
				marked = False
				break
		idx += 1
	return idx

rotated = Image.new('RGB', (640,480))
rotpx   = rotated.load()

for z in range(480):
	offset = find_colidx(z)
	for j in range(640):
		rotpx[j,z] = px[(offset+j)%640,z]

rotated.show() # romance
