"""
http://www.pythonchallenge.com/pc/rock/arecibo.html

title: etch-a-sketch

Fill in the blanks

<!-- you are in level 32 -->

Fill in the blanks <!-- for warmup.txt -->


  <script type="text/javascript" src="etch-a-scetch.js"></script>
  <script type="text/javascript" src="pencil.js"></script>

warmup.txt

# Dimensions
9 9

# Horizontal
2 1 2
1 3 1
5

7
9
3

2 3 2
2 3 2
2 3 2

# Vertical
2 1 3
1 2 3
3

8
9
8

3
1 2 3
2 1 3

# manual solution : shows arrow facing up

http://www.pythonchallenge.com/pc/rock/up.html

" You want to go up? Let's scale this up then. Now get serious and solve this. "
http://www.pythonchallenge.com/pc/rock/up.txt


"""

h_rules = []
v_rules = []

def score_line(line):
	res = []
	c = 0
	for idx, val in enumerate(line):
		if val == 1:
			c += 1
		elif c > 0:
			res.append(c)
			c = 0
	if c > 0:
		res.append(c)
	return res

def score_row(grid, i):
	return score_line(grid[i])

def score_col(i):
	line = []
	for j in range(len(grid)):
		line.append(grid[j][i])
	return score_line(line)

def score_grid(grid):
	for i in range(len(grid)):
		if score_row(grid, i) != h_rules[i]:
			return False
	#for i in range(len(grid[0])):
	#	if score_col(i) != v_rules[i]:
	#		return False
	return True

def transpose(m):
	n = []
	for i in range(len(m)):
		n.append([ x[i] for x in m ])
	return n

def genlines(rules, length, prev=[]):
	if len(prev) == length and len(rules) == 0:
		yield prev
	if (len(prev) + sum(rules) + len(rules) - 1) <= length:
		for _ in genlines(rules, length, prev=prev+[0]):
			yield _
		if len(rules) > 0:
			m = 1 if len(rules) > 1 else 0
			for _ in genlines(rules[1:], length, prev=prev+[1]*rules[0]+[0]*m):
				yield _

def genboard(poss, res=[]):
	if len(poss) == 0:
		yield res
		return
	for x in poss[0]:
		for y in genboard(poss[1:], res=res+[x]):
			yield y

def find_unis(ruleset):
	flt = []
	for i in range(len(ruleset[0])):
		flt.append((i,set()))
	
	for rule in ruleset:
		for i in range(len(flt)):
			flt[i][1].add(rule[i])

	flt = [ x for x in flt if len(x[1]) == 1 ]

	return flt	


with open("up.txt", 'r') as infile:
	vert = False
	horz = False
	for line in infile.readlines():
		if "# Horizontal" in line.strip():
			horz = True
			vert = False
		elif "# Vertical" in line.strip():
			vert = True
			horz = False
		elif vert == True and line.strip() != '':
			v_rules.append([int(x) for x in line.strip().split(' ')])
		elif horz == True and line.strip() != '':
			h_rules.append([int(x) for x in line.strip().split(' ')])

#for i in range(len(v_rules)):
#	grid.append([0] * len(h_rules))

#print(len(v_rules))

v = []
for rule in v_rules:
	v.append([line for line in genlines(rule, len(v_rules))])

h = []
for rule in h_rules:
	h.append([line for line in genlines(rule, len(h_rules))])

#for line in v:
#	print(len(line))

#for line in h:
#	print(len(line))

"""
# Brute Force Solution
for _ in genboard(v[:]):
	if score_grid(transpose(_)):
		for line in transpose(_):
			print(''.join([str(x) for x in line]).replace('1', 'X').replace('0', ' '))
"""

solved = False
while not solved:

	# v_idx[i] impacts hrules[i] at v_idx

	h_filter = [ (v_idx, find_unis(rule)) for v_idx, rule in enumerate(v) if len(find_unis(rule)) > 1 ]

	for v_idx, rules in h_filter:
		#print(v_idx, rules)
		for rule in rules:
			h[rule[0]] = [ x for x in h[rule[0]] if x[v_idx] == tuple(rule[1])[0] ]				

	v_filter = [ (h_idx, find_unis(rule)) for h_idx, rule in enumerate(h) if len(find_unis(rule)) > 1 ]

	for h_idx, rules in v_filter:
		#print(h_idx, rules)
		for rule in rules:
			v[rule[0]] = [ x for x in v[rule[0]] if x[h_idx] == tuple(rule[1])[0] ]
	if sum([ len(x) for x in v ]) == len(v) and sum([ len(x) for x in h ]) == len(h):
		solved = True


for line in h:
	print(''.join([str(x) for x in line[0]]).replace('1', 'X').replace('0', ' '))


"""
                   XXX XX       
                  XXXXXXXX      
                 XXXXXXXXXX     
                 XXX   X  X     
                 XXXXX XX X     
                 XXXXX XX X     
                XXXX   X  X     
             XXXXXXXXXXXXXXX    
           XXXXXXXXXXXXXXXXXXX  
          XXXXXX XXXXXXXXXXXXXX 
         XXXXXX   X XXXXXXXXXXXX
         XXXXXX     X XXXXXXXXXX
        XXXXXXX   XX  X XXXXXXXX
        XXXXXX X X XX   X X X  X
        XXXXX   X  XXXX        X
        XXXXX XXXX X XXXX X X X 
        XXXXX   X X   XXXXXXXX  
         XXXXX XX  X   XXXXXXXX 
         XXXXXX  X  XX   X XXX  
          XXXXXX XXX  XX     X  
           XXXXXX   X   XXXXX   
X           XXXXXX  XXX         
XX           XXXXXXX   XX       
XXX  XXX   XXXXXXXXXX XXXX      
XXXXXXXXX XXXXXXXXXXXX    X     
XXXXXXXXXXXXXXXXXXXXXX    X     
 XXXXXXXXXXXXXXXXXXXXX XXXX     
  X  XXXXXXXXXXXXXXXXX    X     
   XX  XXXXXXXX XXXXX     X     
        XX     XX     XXXX      
          XXXXX  XX X   X       
                   XXXXX        
"""




	
	




