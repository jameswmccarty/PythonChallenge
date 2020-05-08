"""
http://www.pythonchallenge.com/pc/ring/guido.html

title: silence!
picture: whoisit.jpg

"""

#from PIL import Image
#from PIL.ExifTags import TAGS

#im = Image.open('whoisit.jpg')

#exif_data = dict()
#for k,v in im._getexif().items():
#	exif_data[TAGS.get(k)] = v

import urllib.request
import base64
import bz2

auth = "Basic " + base64.b64encode(b"repeat:switch").decode("utf-8") 
r = urllib.request.Request('http://www.pythonchallenge.com/pc/ring/guido.html')
r.add_header("Authorization",auth)
with urllib.request.urlopen(r) as f:
	page = f.read().decode("utf-8")

lines = [len(line) for line in page.split('\n') if line.strip() == '']
print(bz2.decompress(bytes(lines)).decode())		
