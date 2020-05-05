"""
http://www.pythonchallenge.com/pc/hex/ambiguity.html
"""

from PIL import Image
from PIL import ImageDraw
from collections import deque

im = Image.open("./maze.png")
#print(im.size)
x_size, y_size = im.size
maze = im.load()

x = 639 # start point at the top row
y = 0
seen = set()
q = deque()
q.append((x, y, list()))
pairs = []
white = (255, 255, 255, 255)
ended = False

# conduct BFS search through maze
while len(q) > 0 and not ended:
	x, y, path = q.popleft()
	if y == 640 and x == 1: #end point in bottom left
		#print("Solved")
		path.append((x,y))
		pairs = path[:]
		ended = True
		break
	path.append((x,y))
	if x < x_size-1 and (x+1,y) not in seen and maze[x+1, y] != white:
		q.append((x+1, y, path[:]))
		seen.add((x+1, y))
	if x > 0 and (x-1,y) not in seen and maze[x-1, y] != white:
		q.append((x-1, y, path[:]))
		seen.add((x-1, y))
	if y < y_size-1 and (x,y+1) not in seen and maze[x, y+1] != white:
		q.append((x, y+1, path[:]))
		seen.add((x,y+1))
	if y > 0 and (x,y-1) not in seen and maze[x, y-1] != white:
		q.append((x,y-1, path[:]))
		seen.add((x,y-1))

#print(len(pairs))
#draw.line(tuple(pairs),fill=128,width=1)

"""
Attempt to use pixel data along the path to make a new image.
# fails, 44623 is prime.  Tried without final point of size 44622
for any shape that is a rectagle, but nothing is there.
"""
"""
factors = []
for i in range(1,len(pairs)):
	if len(pairs) % i == 0:
		factors.append(i)
print(factors)

for factor in factors:
	test_width = factor
	im2 = Image.new('RGB', (test_width, len(pairs)//test_width))
	dpx = im2.load() # draw on new image
	i = 0
	j = 0
	for pair in pairs:
		dpx[i, j] = maze[pair[0],pair[1]]
		i += 1
		if i == test_width:
			j += 1
			i = 0
	im2.show()
"""

"""
Treat red channel as binary data
 - Every other byte produces a valid zip file
"""
toggle = 0
data = b''
#data2 = b''
for pair in path:
	if toggle == 1:
		data += bytes([maze[pair[0],pair[1]][0]])
		toggle = 0
	else:
		toggle += 1
#		data2 += bytes([maze[pair[0],pair[1]][0]])
with open("24.zip", 'wb') as outfile: # makes valid zip
	outfile.write(data)
#with open("24-2_out", 'wb') as outfile: # zeros
#	outfile.write(data2)
