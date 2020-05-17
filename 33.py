"""
http://www.pythonchallenge.com/pc/rock/beer.html

title: 33 bottles of beer on the wall

image: http://www.pythonchallenge.com/pc/rock/beer1.jpg
(bottles of Jack Daniel's)

<!--
If you are blinded by the light,
remove its power, with its might.
Then from the ashes, fair and square,
another truth at you will glare.
-->

# http://www.pythonchallenge.com/pc/rock/beer2.jpg 'no png'
# http://www.pythonchallenge.com/pc/rock/beer2.png

"""

from PIL import Image
import math
import time

im = Image.open("beer2.png")
data = list(im.getdata())


for i in range(32):
	m = max(data)
	data = [x for x in data if x < m - 1]
	s = int(math.sqrt(len(data)))
	im2 = Image.new('L', (s, s))
	im2.putdata(data)
	im2.show()
	time.sleep(2)


# http://www.pythonchallenge.com/pc/rock/gremlins.html
