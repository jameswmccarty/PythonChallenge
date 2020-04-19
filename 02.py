"""
http://www.pythonchallenge.com/pc/def/map.html
"""

hint = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

"""
ignore = [" ",".","(",")","'"]
for i in range(26):
	out = ''
	for char in hint:
		if char in ignore:
			out += char
		else:
			out += chr((((ord(char)-97)+i) % 26) + 97)
	print(i, out)

# 2 i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

"""

ignore = [" ",".","(",")","'"]
out = ''
for char in hint:
	if char in ignore:
		out += char
	else:
		out += chr((((ord(char)-97)+2) % 26) + 97)

trans = str.maketrans(hint, out)

url = "http://www.pythonchallenge.com/pc/def/"
page = "map"
print(url + page.translate(trans) + ".html")
