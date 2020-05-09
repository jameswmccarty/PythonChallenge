"""
http://www.pythonchallenge.com/pc/ring/yankeedoodle.html

title: relax you are on 30
photo: yankeedoole.jpg (beach photo)

<!-- while you look at the csv file -->
http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv
"""

from PIL import Image

data = []

with open('yankeedoodle.csv', 'r') as infile:
	for line in infile.readlines():
		line = line.strip().split(',')
		data += [float(x) for x in line if x != '']		

im = Image.new('L', (53, 139))
sp = im.load()
for i in range(53):
	for j in range(139):
		sp[i, j] = int(data[j*53+i]*256)
# im.save('float.png')
"""
Needs to be flipped horizontal and rotated 90 degrees.  Shows:
n = str(x[i])[5] + str(x[i+1])[5] + str(x[i+2])[6]
"""
data = []
with open('yankeedoodle.csv', 'r') as infile:
	for line in infile.readlines():
		line = line.strip().split(',')
		data += [x.strip() for x in line if x != '']
n = ''
for i in range(0,len(data)-3,3):
	c = data[i][5] + data[i+1][5] + data[i+2][6]
	n += chr(int(c))
print(n)	
