"""
http://www.pythonchallenge.com/pc/return/romance.html
"""
# picture is of cookies
# the picture of the saw is back on puzzle 4 (http://www.pythonchallenge.com/pc/def/linkedlist.php)

import urllib.request
import requests
import bz2
import urllib.parse
import xmlrpc.client
from http import cookies

seen = [
#("","/def/0.html"),
#("","/def/map.html"),
#("","def/ocr.html"),
("","/def/linkedlist.php"),
#("","/def/peak.html"),
#("","/def/oxygen.html"),
#("","/def/integrity.html"),
#("huge:file@","return/good.html"),
#("huge:file@","return/bull.html"),
#("huge:file@","return/5808.html"),
#("huge:file@","return/evil.html"),
#("huge:file@","return/disproportional.html"),
#("huge:file@","return/italy.html"),
#("huge:file@","return/uzi.html"),
#("huge:file@","return/mozart.html"),
#("huge:file@","return/romance.html"),]
]

for auth,site in seen:
	session = requests.Session()
	response = session.get('http://'+auth+'www.pythonchallenge.com/pc/'+site)
	print(site, response)
	print(session.cookies.get_dict())

# {'info': 'you+should+have+followed+busynothing...'} --> http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=0

nothing = "12345" #initial starting value from problem 4
outmsg = b''
firstplus = True # hack...bz2 encoding issue...fixed by removing first plus sign found in encoded string back from server
for i in range(400):
	f = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=" + nothing)
	session = requests.Session()
	response = session.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=" + nothing)
	outmsg += urllib.parse.unquote_to_bytes(session.cookies.get_dict()["info"])
	next = str(f.read().decode(encoding="utf-8"))
	print(next)
	next = next.split(" ")
	nothing = next[-1]
	try:
		test = int(nothing)
	except:
		print(outmsg)
		newout = b''
		for byte in outmsg:
			if bytes([byte]) == b'+' and firstplus == True:
				newout += b' '
				firstplus = False
			else:
				newout += bytes([byte])
		print(bz2.decompress(newout))
		break

"""
b'is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.'
"""

server_url = "http://www.pythonchallenge.com/pc/phonebook.php"
proxy = xmlrpc.client.ServerProxy(server_url)
try:
	print(proxy.phone('Leopold')) #555-VIOLIN.  Leopold was Mozart's Father's name
except xmlrpc.client.ProtocolError as err:
	print("A protocol error occurred")
	print("URL: %s" % err.url)
	print("HTTP/HTTPS headers: %s" % err.headers)
	print("Error code: %d" % err.errcode)
	print("Error message: %s" % err.errmsg)

server_url = "http://www.pythonchallenge.com/pc/stuff/violin.php"

f = requests.get(server_url, cookies={'info':'the+flowers+are+on+their+way'}).text
print(f) #oh well, don't you dare to forget the balloons.
