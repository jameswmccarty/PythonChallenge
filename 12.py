"""
http://www.pythonchallenge.com/pc/return/evil.html
"""
# the file evil2.gfx is shuffled binary data from various images.
# must split and write out into various files.

shuffle_guess = 5 # trial and error
imgs = [b''] * shuffle_guess
idx  = 0
with open("evil2.gfx", 'rb') as infile:	
	for byte in infile.read():
		imgs[idx%shuffle_guess] += bytes([byte])
		idx += 1

idx = 0
ext = ['.jpg','.png','.gif','.gif','.jpg'] # trial and error
for img in imgs:
	f = open(str(idx)+ext[idx], 'wb')
	f.write(img)
	f.close()
	idx += 1

# spells 'disproportionality' (with ity struck out) -> 'disproportional'
