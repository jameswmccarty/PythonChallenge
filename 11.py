"""
http://www.pythonchallenge.com/pc/return/5808.html
"""
from PIL import Image, ImageDraw
im = Image.open("cave.jpg")
px = im.load()
#imo = Image.new('RGB', (320,240))
#imop = imo.load()
ime = Image.new('RGB', (320,240))
imep = ime.load()
for i in range(320):
	for j in range(240):
		imep[i,j] = px[i*2,j*2]
		#imop[i,j] = px[i*2+1,j*2+1]
ime.show() #evil
#imo.show()



