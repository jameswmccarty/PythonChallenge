import zipfile

"""
Setup: unzip channel.zip.  Copy channel.zip into extracted folder.  Run 06.py from same location.
"""

out = ''

with zipfile.ZipFile('channel.zip', 'r') as myzip:
	#for myfile in myzip.namelist():
	#	with myzip.open(myfile, 'r') as infile:
	#		print(myzip.getinfo(myfile).comment)

	num = 90052
	total = num
	while True:
		with open(str(num)+".txt", 'r') as infile:
			next = infile.readline().strip()
			out += myzip.getinfo(str(num)+'.txt').comment.decode("utf-8")
			#print(next)
			if "Collect" not in next:
				num = int(next.replace("Next nothing is ",''))
				total *= num
			else:
				break
print(out)
# hockey.html -> oxygen.html
