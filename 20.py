"""
http://www.pythonchallenge.com/pc/hex/idiot2.html
"""

import urllib.request
import base64

def next_idx(headers):
	# Content-Range: bytes 30203-30236/2123456789
	for (k,v) in headers:
		if k == 'Content-Range':
			l, r = v.split("/")
			l, r = l.split("-")
	return int(r)+1

auth = "Basic " + base64.b64encode(b"butter:fly").decode("utf-8") 

r = urllib.request.Request('http://www.pythonchallenge.com/pc/hex/unreal.jpg')
r.add_header("Authorization",auth)

with urllib.request.urlopen(r) as f:
	#output = f.read() # JPEG image
	print(f.headers)

while True:
	data_idx = next_idx(f.getheaders())
	r = urllib.request.Request('http://www.pythonchallenge.com/pc/hex/unreal.jpg')
	r.add_header("Authorization",auth)
	r.add_header("Range","bytes="+str(data_idx)+"-2123456789/*")

	try:
		with urllib.request.urlopen(r) as f:
			print(f.read())
			print(f.headers)
	except:
		print(f.headers)
		print(f.status)
		print(f.reason)
		print(f.read())
		#print("Data Idx "+str(data_idx))
		break

"""
http://www.pythonchallenge.com/pc/hex/invader.html
"""
data_idx = 2123456789 - 1
r = urllib.request.Request('http://www.pythonchallenge.com/pc/hex/unreal.jpg')
r.add_header("Authorization",auth)
r.add_header("Range","bytes="+str(data_idx)+"-2123456789/*")

with urllib.request.urlopen(r) as f:
	print(f.read())
	print(f.headers)

# b'esrever ni emankcin wen ruoy si drowssap eht\n'
# the password is your new nickname in reverse

data = b''

data_idx = 2123456744 - 1

while True:

	auth = "Basic " + base64.b64encode(b"butter:fly").decode("utf-8") 
	r = urllib.request.Request('http://www.pythonchallenge.com/pc/hex/unreal.jpg')
	r.add_header("Authorization",auth)
	r.add_header("Range","bytes="+str(data_idx)+"-2123456743/2123456789")

	try:
		with urllib.request.urlopen(r) as f:
			print(f.read())
			print(f.headers)
			break
	except:
		data_idx -= 1
		#print(data_idx)

# b'and it is hiding at 1152983631.\n'

data_idx = 1152983631
auth = "Basic " + base64.b64encode(b"butter:fly").decode("utf-8") 
r = urllib.request.Request('http://www.pythonchallenge.com/pc/hex/unreal.jpg')
r.add_header("Authorization",auth)
r.add_header("Range","bytes="+str(data_idx)+"-*/2123456789")

with urllib.request.urlopen(r) as f:
	output = f.read()
	print(f.headers)

with open('20_out.zip', 'wb') as outfile:
	outfile.write(output)
	

