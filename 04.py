"""
http://www.pythonchallenge.com/pc/def/linkedlist.php
"""

import urllib.request

"""
nothing = "12345"

for i in range(400):
	f = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing)
	next = str(f.read().decode(encoding="utf-8"))
	print(next)
	nothing = str(int(next[-5:]))

# and the next nothing is 16044
# Yes.  Divide by two and keep going
"""

nothing = "8022"

for i in range(400):
	f = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing)
	next = str(f.read().decode(encoding="utf-8"))
	print(next)
	next = next.split(" ")
	nothing = next[-1]
	try:
		test = int(nothing)
	except:
		print("http://www.pythonchallenge.com/pc/def/" + nothing)
		exit()
