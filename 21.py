"""
21.zip 

(password 'redavni')

- readme.txt
Yes! This is really level 21 in here. 
And yes, After you solve it, you'll be in level 22!

Now for the level:

* We used to play this game when we were kids
* When I had no idea what to do, I looked backwards.

- package.pack

zlib compressed data?

"""

"""
# Check for comments in zipfile
import zipfile
with zipfile.ZipFile('21.zip', 'r') as myzip:
	for myfile in myzip.namelist():
		with myzip.open(myfile,pwd=b'redavni', mode='r') as infile:
			print(myzip.getinfo(myfile).comment)
"""

import zipfile
import zlib
import bz2

with zipfile.ZipFile('21.zip', 'r') as myzip:
	with myzip.open("package.pack",pwd=b'redavni', mode='r') as infile:
		data = infile.read()

second_fail = False
while True:
	try:
		data = zlib.decompress(data)
		second_fail = False
		print(" ",end='')
	except:
		try:
			data = bz2.decompress(data)
			print("0",end='')
			second_fail = False
		except:
			if second_fail:
				break
			else:
				data = bytearray(data)
				data.reverse()
				data = bytes(data)
				print("")
				second_fail = True

"""
      000          000      00000000    00000000    0000000000  00000000
    0000000      0000000    000000000   000000000   000000000   000000000
   00     00    00     00   00      00  00      00  00          00      00
  00           00       00  00      00  00      00  00          00      00
  00           00       00  000000000   000000000   00000000    000000000
  00           00       00  00000000    00000000    00000000    00000000 
  00           00       00  00          00          00          00   00 
   00     00    00     00   00          00          00          00    00 
    0000000      0000000    00          00          000000000   00     00 
      000          000      00          00          0000000000  00      00
"""

with open("./package.pack.txt", 'wb') as outfile:
	outfile.write(data) # "look at your logs"

#http://www.pythonchallenge.com/pc/hex/copper.html
