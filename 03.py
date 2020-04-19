"""
http://www.pythonchallenge.com/pc/def/equality.html
"""

total = ''
out = ''
with open('equality.txt' ,'r') as infile:
	for line in infile.readlines():
		total += line.strip()
for idx in range(4,len(total)-4):
	if total[idx-4].islower() and total[idx-3:idx].isupper() and total[idx].islower() and total[idx+1:idx+4].isupper() and total[idx+4].islower():
		out+=total[idx]

url = "http://www.pythonchallenge.com/pc/def/"
print(url + out + ".html")


