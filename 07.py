"""
http://www.pythonchallenge.com/pc/def/oxygen.html
"""

last = 0
#crop oxygen.png to 1 pixel tall image, only gray squares
#save as oxygen.ppm
with open('oxygen.ppm', 'r') as infile:
	for line in infile.readlines():
		if int(line.strip()) != last:
			last = int(line.strip())
			print(chr(last), end='')
print()

#z = [105, 10, 16, 101, 103, 14, 105, 16, 121]
z = [105, 110, 116, 101, 103, 114, 105, 116, 121]

for item in z:
	print(chr(item),end='')
print()

#http://www.pythonchallenge.com/pc/def/integrity.html
