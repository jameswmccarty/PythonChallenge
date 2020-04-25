"""
http://www.pythonchallenge.com/pc/return/balloons.html
# can you tell the difference?
http://www.pythonchallenge.com/pc/return/brightness.html
# maybe consider delta.gz
"""

from PIL import Image, ImageDraw
import gzip, difflib

"""

https://en.wikipedia.org/wiki/Portable_Network_Graphics

89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52
00 00 00 01 00 00 00 01 08 02 00 00 00 90 77 53
DE 00 00 00 0C 49 44 41 54 08 D7 63 F8 CF C0 00
00 03 01 01 00 18 DD 8D B0 00 00 00 00 49 45 4E
44 AE 42 60 82
	

.PNG........IHDR
..............wS
.....IDAT..c....
.............IEN
D.B`. 

"""

#start_mark = "89 50 4E 47 0D 0A 1A 0A".lower()
#end_mark = "00 00 00 00 49 45 4E 44 AE 42 60 82".lower()

"""
im = Image.open("balloons.jpg")
#print(im.getbbox())
px = im.load()
l = Image.new('RGB', (375,335))
lp = l.load()
r = Image.new('RGB', (375,335))
rp = r.load()
d = Image.new('RGB', (375,335))
dp = d.load()
for i in range(375):
	for j in range(335):
		lp[i,j] = px[i,j]
		rp[i,j] = px[i+375,j]
		dp[i,j] = (abs(lp[i,j][0]-rp[i,j][0]),abs(lp[i,j][1]-rp[i,j][1]),abs(lp[i,j][2]-rp[i,j][2]))

l.save("left.png")
r.save("right.png")
d.save("diff.png")

"""

deltas = gzip.open("deltas.gz")
l_block = []
r_block = []
for line in deltas:
	l_block.append(line.decode()[:56].strip())
	r_block.append(line.decode()[56:].strip())

compare = difflib.Differ().compare(l_block, r_block)

l_only = []
r_only = []
l_and_r = []

for line in compare:
	if '-' in line and len(line.strip()) > 1:
		l_only.append(line.replace('-','').strip())
	elif '+' in line and len(line.strip()) > 1:
		r_only.append(line.replace('+','').strip())
	else:
		l_and_r.append(line.replace('-','').strip())

for i,f in enumerate([l_only, r_only, l_and_r]):
	b_o = b''
	b_in = " ".join(f).strip()
	b_in = b_in.strip().split(" ")
	b_in = [int(x,16) for x in b_in]
	for val in b_in:
		b_o += val.to_bytes(1,'little')

	with open(str(i)+'.png', 'wb') as outfile:
		outfile.write(b_o)

# /hex/bin.html
# butter
# fly
