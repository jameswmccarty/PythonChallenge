"""
http://www.pythonchallenge.com/pc/return/bull.html
"""
# sequence.txt
# > a = [1, 11, 21, 1211, 111221, 
# hint
# > len(a[30]) = ?

"""
Verbal riddle sequence.  Spoken out loud.
"1"
"One 1"
"Two 1"
"One 2 Two 1", etc
"""
def gen_next(seq):
	out = ''
	cur = seq[0]
	count = 1
	seq = seq[1:]
	while len(seq) > 0:
		if len(seq) > 0 and seq[0] == cur:
			count += 1
		else:
			out = out + str(count) + cur
			if len(seq) > 0:
				cur = seq[0]
				count = 1
		seq = seq[1:]
	out = out + str(count) + cur		
	#print(out)
	return out
	


current = "1"
for i in range(30):
	current = gen_next(current)
print(len(current)) #5808
