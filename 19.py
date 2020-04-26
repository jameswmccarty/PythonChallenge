"""
http://www.pythonchallenge.com/pc/hex/bin.html
"""

import base64

"""
Field 	Length 	Contents
ckID 	4 	Chunk ID: "RIFF"
cksize 	4 	Chunk size: 4+n
	WAVEID 	4 	WAVE ID: "WAVE"
	WAVE chunks	n 	Wave chunks containing format information and sampled data
"""

with open("attachment.txt", 'r') as infile:
	att = ''
	for line in infile.readlines():
		att += line.strip()

song = bytearray(base64.b64decode(att))

with open("indian.wav", 'wb') as outfile:
	outfile.write(bytes(song)) # speaks 'sorry'

# hint is Indian sounds like 'Endian'
# flip the byte orders...

#print(song[0:4].decode("utf-8"))
for i in range(44,len(song),2): # preserve header
	t = song[1+i]
	song[1+i] = song[i]
	song[i] = t 

with open("indian2.wav", 'wb') as outfile:
	outfile.write(bytes(song)) # speaks 'you are an idiot'


# http://www.pythonchallenge.com/pc/hex/sorry.html
# - "what are you apologizing for?"
# http://www.pythonchallenge.com/pc/hex/india.html
# nnn. what could this mean?
# http://www.pythonchallenge.com/pc/hex/idiot.html
# http://www.pythonchallenge.com/pc/hex/idiot2.html
