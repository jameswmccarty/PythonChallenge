"""
http://www.pythonchallenge.com/pc/def/peak.html
"""

import pickle

with open('banner.p', 'rb') as f:
	data = pickle.load(f)

for i in range(len(data)):
	for item in data[i]:
		for x in range(item[1]):
			print(item[0], end='')
	print()

#channel
#http://www.pythonchallenge.com/pc/def/channel.html
