"""
http://www.pythonchallenge.com/pc/hex/lake.html

<img src="lake1.jpg"> <!-- can you see the waves? --> 'imagine how they sound'

# 25 files, lake1.wav through lake25.wav
http://www.pythonchallenge.com/pc/hex/lake1.wav
...
http://www.pythonchallenge.com/pc/hex/lake25.wav

* Treat the wave files as raw binary data.
* All the files are of length 10844 bytes.
* The WAV header is 44 bytes
* With 3x 8-bit channels per pixel, there are
* 10800 / 3 = 3600 pixels in each WAV file.
* That will form a 60x60 pixel square

* With 25 files, that is a 5x5 grid of 60*60 sub-images.

"""
from PIL import Image

composite = Image.new('RGB', (60*5,60*5))
imp       = composite.load()

for _ in range(1,26):
	with open("./lake/lake"+str(_)+".wav", 'rb') as infile:
		data = infile.read()
	data = bytearray(data)
	data = data[44:]

	bx = ((_-1) // 5) * 60
	by = ((_-1) %  5) * 60
	idx = 0
	for i in range(60):
		for j in range(60):
			imp[bx+i,by+j] = (data[idx], data[idx+1], data[idx+2])
			idx += 3
composite.save("./lake_out.png") # spells 'decent'
