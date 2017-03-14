import random

def roll(num, sides):
	val = 0
	if num:
		for i in range(num):
			val += random.randint(1, sides)
		return val
	return random.randint(1, sides)

def stats():
	s = []
	for i in range(1,7):
		short = []
		for x in range(1, 5):
			#r = roll(0,6)
			#print(r)
			short.append(roll(0,6))
		short.sort()
		s.append(sum(short[1:]))
	s.sort()
	print(s)

while True:
	inp = input('Enter the dice roll (q to quit, s for stats): ')
	if inp.lower() == 'q' or inp.lower() == 'quit':
		exit()
	if inp.lower() == 's':
		stats()
		continue
	s = inp.split('d')
	if len(s) < 2:
		print ('%s  :  %d' %(inp,roll(0,int(s[0]))))
	else:
		print ('%s  :  %d' %(inp,roll(int(s[0]),int(s[1]))))