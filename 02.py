"""
http://www.pythonchallenge.com/pc/def/ocr.html
"""

with open('ocr.txt', 'r') as infile:
	intext = infile.read().strip()
	out = ''	
	for char in intext:
		if ord(char) > 96 and ord(char) < 123:
			out += char

url = "http://www.pythonchallenge.com/pc/def/"
print(url+out+".html")
