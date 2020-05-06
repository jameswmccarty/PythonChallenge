"""
http://www.pythonchallenge.com/pc/hex/decent.html

<title>be a man - apologize!</title>
<!-- you've got his e-mail -->
Hurry up, I'm missing the boat

From puzzle #19:

leopold.moz@pythonchallenge.com

"""

# Sent an e-mail outside of Python.
# Subj: sorry

"""
Date: Tue, 5 May 2020 17:05:20 -0700
From: Leopold Mozart <leopold.moz@pythonchallenge.com>
To: <my e-mail address>
Subject: Re: my broken zip Re: sorry

Never mind that.

Have you found my broken zip?

md5: bbb8b499a0eef99b52c7f13f4e78c24b

Can you believe what one mistake can lead to?
"""

import hashlib
import zipfile

with zipfile.ZipFile('./mybroken.zip', 'r') as myzip:
	print(myzip.testzip()) # mybroken.gif

with open('./mybroken.zip', 'rb') as infile:
	data = infile.read()

h = hashlib.new('md5')
h.update(data)
print(h.hexdigest()) #bbf6616928e23ecfef4b717f281c53cc

data = bytearray(data)

fixed = False
while not fixed:
	for idx in range(len(data)):
		for i in range(255):
			trial = data[:]
			trial[idx] = i
			trial = bytes(trial)
			h = hashlib.new('md5')
			h.update(trial)
			if h.hexdigest() == 'bbb8b499a0eef99b52c7f13f4e78c24b':
				#print(idx, i) # 1234 168
				with open('myfixed.zip', 'wb') as outfile:
					outfile.write(trial)
				fixed = True
				break

# file mybroken.gif says 'speed'

# Investigate how/if mybroken.gif is broken
# File is OK.  Answer is 'speedboat'  (hint: I'm missing the boat)
