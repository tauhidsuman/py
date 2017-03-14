#!/usr/bin/python
"""
This file contains all my solutions to the exercises available on http://www.practicepython.org/
-Austin
"""
import datetime
import random
import math
import timeit

def run():
	exer33()
	
def exer33():
	"""
	For this exercise, we will keep track of when our friend’s birthdays are, and be able to find
	that information based on their name. Create a dictionary (in your file) of names and
	birthdays. When you run your program it should ask the user to enter a name, and return the
	birthday of that person back to them. The interaction should look something like this:

	>>> Welcome to the birthday dictionary. We know the birthdays of:
	Albert Einstein
	Benjamin Franklin
	Ada Lovelace
	>>> Who's birthday do you want to look up?
	Benjamin Franklin
	>>> Benjamin Franklin's birthday is 01/17/1706.
	Happy coding!
	"""
	#with open("data/birthdays.txt", "w+") as f:
	#	f.write("Austin Durand,07/26/1989")
	print("Welcome to the birthday dictionary. We know the birthdays of: ")
	db = {}
	with open("data/birthdays.txt", "r+") as f:
		for l in f:
			db[l.split(',')[0]] = l.split(',')[1]
	for x in db.keys():
		print(x)
	imp = input("Who's birthday do you want to look up? ")
	print(db[imp])
	

def exer32():
	"""
	In this exercise, we will finish building Hangman. In the game of Hangman, the player only has
	6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

	In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the
	logic for guessing the letter and displaying that information to the user. In this exercise, we
	have to put it all together and add logic for handling guesses.

	Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following
	features:

	Only let the user guess 6 times, and tell the user how many guesses they have left.
	Keep track of the letters the user guessed. If the user guesses a letter they already guessed,
	don’t penalize them - let them guess again.
	"""
	#already completed in exer31
	pass

def exer31():
	"""
	Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program
	that the player has to guess, letter by letter. The player guesses one letter at a time until
	the entire word has been guessed. (In the actual game, the player can only guess 6 letters
	incorrectly before losing).

	Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic
	that asks a player to guess a letter and displays letters in the clue word that were guessed
	correctly. For now, let the player guess an infinite number of times until they get the entire
	word. As a bonus, keep track of the letters the player guessed and display a different message
	if the player tries to guess that letter again. Remember to stop the game when all the letters
	have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the
	number of guesses the player has remaining - we will deal with those in a future exercise.

	An example interaction can look like this:
		>>> Welcome to Hangman!
		_ _ _ _ _ _ _ _ _
		>>> Guess your letter: S
		Incorrect!
		>>> Guess your letter: E
		E _ _ _ _ _ _ _ E
		...
	And so on, until the player gets the word.
	"""
	w = exer30()
	left = 6
	made = 0
	guessed = set('')
	print("Welcome to Hangman.")
	while True:
		show = ""
		for i in w:
			if i in guessed:
				show += i
			else:
				show += "_"
			show += " "
		if not "_" in show:
			print("You have won!, the word is %s" %w)
			break
		if left < 1:
			print("You ran out of guesses and lost. The word was %s" %w)
			break
		print(show)
		print("Letters used: " + str(guessed))
		print("You have %d guesses remaining." %left)
		while True:
			inp = input("Please enter a character: ").upper()[0]
			if not inp in guessed:
				guessed.add(inp)
				if not inp in w:
					left -= 1
				break
			else:
				print("Character already used, try again.")
				continue

def exer30():
	"""
	In this exercise, the task is to write a function that picks a random word from a list of words
	from the SOWPODS dictionary. Download this file and save it in the same directory as your
	Python code. This file is Peter Norvig’s compilation of the dictionary of words used in
	professional Scrabble tournaments. Each line in the file contains a single word.
	"""
	with open("data/dictionary.txt", "r") as f:
		lines = 0
		for l in f:
			lines += 1
		def m1(i=0): #slower
			from linecache import getline
			return getline("data/dictionary.txt", i).strip()
		def m2(i=0): #faster
			x = 0
			f.seek(0)
			for l in f:
				if x == (i - 1): return l.strip()
				x += 1
			else:
				print("No results, x = %d" %(x))
		r = random.randint(1,lines)
		return m2(r)

def exer29():
	"""
	This exercise is Part 4 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part
	1, Part 2, and Part 3.

	In 3 previous exercises, we built up a few components needed to build a Tic Tac Toe game in
	Python:
		Draw the Tic Tac Toe game board
		Checking whether a game board has a winner
		Handle a player move from user input

	The next step is to put all these three components together to make a two-player Tic Tac Toe
	game! Your challenge in this exercise is to use the functions from those previous exercises all
	together in the same program to make a two-player game that you can play with a friend. There
	are a lot of choices you will have to make when completing this exercise, so you can go as far
	or as little as you want with it.

	Here are a few things to keep in mind:
		You should keep track of who won - if there is a winner, show a congratulatory message on
		the screen.
		If there are no more moves left, don’t ask for the next player’s move!
	
	As a bonus, you can ask the players if they want to play again and keep a running tally of who
	won more - Player 1 or Player 2.
	"""
	exer27() #already done

def exer28():
	"""
	Implement a function that takes as input three variables, and returns the largest of the three.
	Do this without using the Python max() function!

	The goal of this exercise is to think about some internals that Python normally takes care of
	for us. All you need is some variables and if statements!
	"""
	pass #silly

def exer27():
	"""
	This exercise is Part 3 of 4 of the Tic Tac Toe exercise series. The other exercises are:
	Part 1, Part 2, and Part 4.

	In a previous exercise we explored the idea of using a list of lists as a “data structure” to
	store information about a tic tac toe game. In a tic tac toe game, the “game server” needs to
	know where the Xs and Os are in the board, to know whether player 1 or player 2 (or whoever
	is X and O won).

	There has also been an exercise about drawing the actual tic tac toe gameboard using text
	characters.

	The next logical step is to deal with handling user input. When a player (say player 1, who
	is X) wants to place an X on the screen, they can’t just click on a terminal. So we are going
	to approximate this clicking simply by asking the user for a coordinate of where they want to
	place their piece.

	As a reminder, our tic tac toe game is really a list of lists. The game starts out with an
	empty game board like this:

	game = [[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]]
	The computer asks Player 1 (X) what their move is (in the format row,col), and say they type
	1,3. Then the game would print out

	game = [[0, 0, X],
			[0, 0, 0],
			[0, 0, 0]]
	And ask Player 2 for their move, printing an O in that place.

	Things to note:
	For this exercise, assume that player 1 (the first player to move) will always be X and
	player 2 (the second player) will always be O.
	Notice how in the example I gave coordinates for where I want to move starting from (1, 1)
	instead of (0, 0). To people who don’t program, starting to count at 0 is a strange concept,
	so it is better for the user experience if the row counts and column counts start at 1. This
	is not required, but whichever way you choose to implement this, it should be explained to
	the player.
	Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a
	number. Then you can use your Python skills to figure out which row and column they want
	their piece to be in.
	Don’t worry about checking whether someone won the game, but if a player tries to put a piece
	in a game position where there already is another piece, do not allow the piece to go there.

	Bonus:
	For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of
	how many squares are full. In a bonus version, keep track of how many squares are full and
	automatically stop asking for moves when there are no more valid moves.
	"""
	game = [[0 for i in range(3)] for x in range(3)]
	while True:
		exer24(game)
		if exer26(game): break
		inp = input("You are Player 1 (X). Which spot will you take? (example: 1,2 or 3,1): ").split(',')
		x, y = int(inp[0]), int(inp[1])
		if game[x][y]:
			print("Not a valid move, that spot has already been taken. Try again.")
		else:
			#print(str(game))
			game[x][y] = 1
			#print(str(game))
			if exer26(game): break
			choices = list()
			x,y = 0,0
			for row in game:
				for column in row:
					if column == 0:
						choices.append([x, y])
					x += 1
				y += 1
				x = 0
			#print(str(choices))
			if(len(choices) == 0):
				print("The game is a draw.")
				return
			c = choices[random.randint(0,len(choices) - 1)]
			#print(str(c))
			game[c[1]][c[0]] = 2			

def exer26(game = None):
	"""
	This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are:
	Part 1, Part 3, and Part 4.

	As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this
	is significantly more than half an hour of coding, so we’re doing it in pieces.

	Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not
	worrying about how the moves were made.

	If a game of Tic Tac Toe is represented as a list of lists, like so:

	game = [[1, 2, 0],
			[2, 1, 0],
			[2, 1, 1]]
	where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a
	2 means that player 2 put their token in that space.

	Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
	tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3
	in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO
	people have won - assume that in every board there will only be one winner.
	"""
	if game == None:
		game = [[1, 2, 0],
				[2, 1, 0],
				[2, 1, 1]]
	def same(l):
		if l[0] == l[1] == l[2]: 
			if l[0]:
				#print("DEBUG: Winning list: " + str(l))
				return l[0]
		else: return 0
	def proc():
		zipped = list(zip(game[0],game[1],game[2]))
		for i in game:
			#print("DEBUG: Row: " + str(i))
			if(same(i)): return i[0]
		for i in zipped:
			#print("DEBUG: Column: " + str(i))
			if(same(i)): return i[0]
		if same([game[0][0],game[1][1],game[2][2]]): return game[0][0]
		if same([game[2][0],game[1][1],game[0][2]]): return game[2][0]
	win = proc()
	if win: 
		print("Player %d won." %(win))
		#print(str(game))
		return win


def exer25():
	"""
	In a previous exercise, we’ve written a program that “knows” a number and asks a user to
	guess it.

	This time, we’re going to do exactly the opposite. You, the user, will have in your head a
	number between 0 and 100. The program will guess a number, and you, the user, will say
	whether it is too high, too low, or your number.

	At the end of this exchange, your program should print out how many guesses it took to get
	your number.

	As the writer of this program, you will have to choose how your program will strategically
	guess. A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4,
	etc.) until you hit the number. But that’s not an optimal guessing strategy. An alternate
	strategy might be to guess 50 (right in the middle of the range), and then increase / 
	ecrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! 
	We’ll talk about what is the optimal one next week with the solution.)
	"""
	print("Alright, think of a number between 1 and 100.")
	print("I will guess a few times to find your number, let me know if my guess is too high,")
	print("too low, or right on.")
	def f():
		return ((top - bot)//2) + bot
	top = 100
	bot = 1
	mid = f()
	tries = 0
	while True:
		if tries > 7:
			print("You lied. Or forgot your number... FAIL!")
			exit()
		tries += 1
		print("My current guess is %d." %(mid))
		inp = input("Is this too [high], too [low], or [correct]: ")
		if inp == 'high':
			top = mid
			mid = f()
		elif inp == 'low':
			bot = mid
			mid = f()
		elif inp == 'correct':
			break
		else:
			print("Incorrect response; trying again.")
			continue
	print("I made %d attempts." %(tries))


def exer24(inp = None):
	"""
	This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are:
	Part 2, Part 3, and Part 4.

	Time for some fake graphics! Let’s say we want to draw game boards that look like this:

	 --- --- --- 
	|   |   |   | 
	 --- --- ---  
	|   |   |   | 
	 --- --- ---  
	|   |   |   | 
	 --- --- --- 
	This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for
	chess, 19x19 for Go, and many more).

	Ask the user what size game board they want to draw, and draw it for them to the screen using
	Python’s print statement.
	"""
	h = '   |'
	v = '--- '
	if inp == None:
		inp = input("Please enter a board size (ex. 5x5): ").split('x')
		for i in range(0, (int(inp[1]) * 2) + 1):
			if(i % 2) == 0:
				print(' ' + (v * int(inp[0])))
			else:
				print('|' + (h * int(inp[0])))
	else: #for when the func gets passed a 'square' matrix of ints
		line = ' ' + (v * len(inp[0]))
		for i in inp:
			print(line)
			s = '|'
			for x in i:
				s += ' '
				if x == 0: s += ' '
				elif x == 1: s+= 'X'
				elif x == 2: s+= 'O'
				s += ' |'
			print(s)
		print(line)


def exer23():
	"""
	Given two .txt files that have lists of numbers in them, find the numbers that are
	overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt
	file has a list of happy numbers up to 1000.
	"""
	primes = []
	happyprimes = []
	with open("data/primenumbers.txt", "r") as f:
		for l in f:
			primes.append(int(l))
	with open("data/happynumbers.txt", "r") as f:
		for l in f:
			if int(l) in primes:
				happyprimes.append(l)
	with open("data/happyprimenumbers.txt", "w") as f:
		for n in happyprimes:
			f.write(n)


def exer22():
	"""
	Given a .txt file that has a list of a bunch of names, count how many of each name there are
	in the file, and print out the results to the screen. I have a .txt file for you, if you want
	to use it!

	Extra:
		Instead of using the .txt file from above (or instead of, if you want the challenge),
		take this .txt file, and count how many of each “category” of each image there are. This
		text file is actually a list of files corresponding to the SUN database scene recognition
		database, and lists the file directory hierarchy for the images. Once you take a look at
		the first line or two of the file, it will be clear which part represents the scene
		category. To do this, you’re going to have to remember a bit about string parsing in
		Python 3. I talked a little bit about it in this post.
	"""
	d = {}
	with open("data/Training_01.txt", "r") as f:
		for l in f:
			s = l.split('/')
			name = s[2]
			if not ('.jpg' in s[3]):
				name = name + '-' + s[3]
			if not (name in list(d.keys())):
				d[name] = 1
			else:
				d[name] += 1
	
	with open("data/Training_01_OUTPUT.txt", "w") as f:
		f.write(str(d))
	print("Done.")

def exer21():
	"""
	Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to
	play with some different code, use the code from the solution), and instead of printing the
	results to a screen, write the results to a txt file. In your code, just make up a name for
	the file you are saving to.

	Extras:
		Ask the user to specify the name of the output file that will be saved.
	"""
	inp = input("Enter a file name: ")
	with open(inp + ".txt", "w") as f:
		f.write("I'm lazy and I don't want to do the webpage thing.")


def exer20():
	"""\
	Write a function that takes an ordered list of numbers (a list where the elements are in
	order from smallest to largest) and another number. The function decides whether or not the
	given number is inside the list and returns (then prints) an appropriate boolean.\
	"""
	a = list(range(0,99999, 3))
	find = random.randint(0,max(a))
	def method1():
		top = len(a) - 1
		bot = 0
		cur = top // 2
		while True:
			#print("Top: %d, Bot: %d, Cur: %d" %(top, bot, cur))		
			if find == a[cur]:
				return True
				break
			elif find > a[cur]:
				bot = cur
				cur = ((top - bot) // 2) + bot
			else:
				top = cur
				cur = ((top - bot) // 2) + bot
			if abs((top - bot)) <= 1:
				return False
				break
	
	def method2():
		if find in a: return True
		else: return False

	print("Find %d? %s" %(find,str(method1())))

def exer19():
	"""
	Using the requests and BeautifulSoup Python libraries, print to the screen the full text of
	the article on this website: 
	http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

	The article is long, so it is split up between 4 pages. Your task is to print out the text to
	the screen so that you can read the full article without having to click any buttons.

	(Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries
	through the solution of the exercise posted here.)

	This will just print the full text of the article to the screen. It will not make it easy to
	read, so next exercise we will learn how to write this text to a .txt file.
	"""
	pass #dont care

def exer18():
	"""
	Create a program that will play the “cows and bulls” game with the user. The game works like
	this:

	Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit
	that the user guessed correctly in the correct place, they have a “cow”. For every digit the
	user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess,
	tell them how many “cows” and “bulls” they have. Once the user guesses the correct number,
	the game is over. Keep track of the number of guesses the user makes throughout the game and
	tell the user at the end.

	Say the number generated by the computer is 1038. An example interaction could look like this:

  		Welcome to the Cows and Bulls Game! 
  		Enter a number: 
		>>> 1234
		2 cows, 0 bulls
		>>> 1256
		1 cow, 1 bull
		...
	Until the user guesses the number.
	"""
	print("Welcome to the Cows and Bulls Game!")
	tries = 0
	s = str(random.randint(1000,9999))
	while True:
		inp = input("Please enter your guess: ")
		if (inp == 'exit') or (inp == 'quit') or (inp == 'q'): break
		cows = bulls = 0
		if inp == s:
			print("You got the number!")
			break
		for i in range(0,3):
			if inp[i] == s[i]: cows += 1
			elif inp[i] in s: bulls += 1
		tries += 1
		print("You have %d cow(s) and %d bull(s)." %(cows,bulls))
	print("The number was %s. You finished after making %d tries." %(s,tries))
		

def exer17():
	"""
	Use the BeautifulSoup and requests Python packages to print out a list of all the article
	titles on the New York Times homepage.
	"""
	import requests
	import bs4 as bs
	url = 'https://www.nytimes.com'
	r = requests.get(url)
	html = r.text
	soup = bs.BeautifulSoup(html, "html.parser")
	for story_heading in soup.find_all(class_="story-heading"): 
		if story_heading.a: 
			print(story_heading.a.text.replace("\n", " ").strip())
		else: 
			print(story_heading.contents[0].strip())


def exer16():
	"""
	Write a password generator in Python. Be creative with how you generate passwords - strong
	passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The
	passwords should be random, generating a new password every time the user asks for a new
	password. Include your run-time code in a main method.

	Extra:
	Ask the user how strong they want their password to be. For weak passwords, pick a word or two
	from a list.
	"""
	poss = [chr(i) for i in range(0, 255)]
	#print(str(poss))
	strongpw = u''
	for i in random.sample(poss, 15):
		strongpw += i
	print(strongpw)

def exer15():
	"""
	Write a program (using functions!) that asks the user for a long string containing multiple
	words. Print back to the user the same string, except with the words in backwards order. For
	example, say I type the string:
		My name is Michele
	Then I would see the string:
  		Michele is name My
	shown back to me.
	"""
	s = "My name is Austin"
	l = s.split()
	print(s)
	print(str(l))
	print(str(l[::-1]))

def exer14():
	"""
	Write a program (function!) that takes a list and returns a new list that contains all the
	elements of the first list minus all the duplicates.

	Extras:
		Write two different functions to do this - one using a loop and constructing a list, 
		and another using sets.
	"""
	test = [1, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 10]
	def method1():
		l = []
		for i in test:
			if not (i in l):
				l.append(i)
		return l
	def method2():
		return set(test)
	print(str(test))
	print(str(method1()))
	print(str(method2()))

def exer13():
	"""
	Write a program that asks the user how many Fibonnaci numbers to generate and then generates
	them. Take this opportunity to think about how you can use functions. Make sure to ask the
	user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence
	is a sequence of numbers where the next number in the sequence is the sum of the previous two
	numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
	"""
	inp = int(input("How many Fibonnaci numbers do you want: "))
	l = [0, 1]
	while True:
		x = len(l) - 1
		l.append(l[x] + l[x - 1])
		if(len(l) == inp):
			break
	print("Your numbers-")
	print(str(l))
		

def exer12():
	"""
	Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes
	a new list of only the first and last elements of the given list. For practice, write this
	code inside a function.
	"""
	a = [5, 10, 15, 20, 25]
	b = [a[0], a[-1]]
	print(str(b))

def exer11():
	"""
	Ask the user for a number and determine whether the number is prime or not. (For those who
	have forgotten, a prime number is a number that has no divisors.). You can (and should!) use
	your answer to Exercise 4 to help you. Take this opportunity to practice using functions,
	described below.
	"""
	#inp = int(input("Enter a number: "))
	inp = 100000 #for speed testing
	def method1():
		l = list(range(3, inp, 2))
		r = [3]
		for i in l:
			for x in r:
				if not (i % x):
					break
			else:
				r.append(i)
		return r
	def method2(max_n): #sundaram3
		numbers = list(range(3, max_n, 2))
		half = (max_n)//2
		initial = 4

		for step in range(3, max_n, 2):
			for i in range(initial, half, step):
				numbers[i-1] = 0
			initial += 2*(step+1)

			if initial > half:
				return [2] + list(filter(None, numbers))
	print("Prime numbers found up to " + str(inp))
	print(str(method1()))

def exer10():
	"""
	This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except 
	require the solution in a different way.

	Take two lists, say for example these two:
		a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
		b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	and write a program that returns a list that contains only the elements that are common
	between the lists (without duplicates). Make sure your program works on two lists of different
	sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember
	list comprehensions from Exercise 7).

	The original formulation of this exercise said to write the solution using one line of Python,
	but a few readers pointed out that this was impossible to do without using sets that I had not
	yet discussed on the blog, so you can either choose to use the original directive and read
	about the set command in Python 3.3, or try to implement this on your own and use at least one
	list comprehension in the solution.

	Extra:
		Randomly generate two lists to test this
	"""
	pass #acccomplished in exer5()

def exer9():
	"""
	Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess
	the number, then tell them whether they guessed too low, too high, or exactly right.
	(Hint: remember to use the user input lessons from the very first exercise)

	Extras:
		Keep the game going until the user types “exit”
		Keep track of how many guesses the user has taken, and when the game ends,
		print this out.
	"""
	num = random.randint(1,9)
	tries = 0
	while True:
		inp = input("Please enter your number guess: ")
		if (inp == 'exit') or (inp == 'quit') or (inp == 'q'): break
		inp = int(inp)
		if inp == num:
			print("You guessed correctly after %d tries!" %(tries))
			print("A new number has been generated.")
			num = random.randint(1,9)
			tries = 0
		elif inp > num:
			print("Your guess is higher than the number.")
			tries = tries + 1
		else:
			print("Your guess is lower than the number.")
			tries = tries + 1
	print("You quit after %d tries on the current number (%d)." %(tries, num))

def exer8():
	"""
	Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), 
	compare them, print out a message of congratulations to the winner, and ask if the 
	players want to start a new game)

	Remember the rules:
		Rock beats scissors
		Scissors beats paper
		Paper beats rock
	"""
	GAME = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}
	#dict with object as the key, and the thing it beats as the value
	while True:
		inp = input("Rock, paper, or scissors: ").lower()
		if (inp == 'exit') or (inp == 'quit') or (inp == 'q'): break
		comp = list(GAME.keys())[random.randint(0,2)]
		print("Computer randomly chose " + comp)
		if inp == comp:
			print("Tie!")
		elif inp == GAME[comp]:
			print("You lost!")
		else:
			print("You won!")

def exer7():
	"""
	Let’s say I give you a list saved in a variable: 
	a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
	Write one line of Python that takes this list a and makes a new list that has 
	only the even elements of this list in it.
	"""
	a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	b = [x for x in a if (x % 2) == 0]
	print("Evenly numbered list-\n" + str(b))

def exer6():
	"""
	Ask the user for a string and print out whether this string is a palindrome
	or not. (A palindrome is a string that reads the same forwards and backwards.)
	"""
	inp = input("Give me a possible palindrome: ")
	flip = inp[::-1]
	if flip.lower() == inp.lower():
		print("Palindrome!")
	else:
		print("Not a palindrome :(")
	print("Flipped string: " + flip)

def exer5():
	"""
	Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	and write a program that returns a list that contains only the elements that are common
	between the lists (without duplicates). Make sure your program works on two lists of
	different sizes.

	Extras:
		Randomly generate two lists to test this
		Write this in one line of Python (don’t worry if you can’t figure this out
		at this point - we’ll get to it soon)
	"""
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]	
	#ans = set(y for x in a for y in b if x == y)
	ans = [x for x in set(a) if x in b]
	print("Set a: " + str(a))
	print("Set b: " + str(b))
	print("Set of like numbers: " + str(ans))

def exer4():
	"""
	Create a program that asks the user for a number and then prints out a list of all the
	divisors of that number. (If you don’t know what a divisor is, it is a number that divides
	evenly into another number. For example, 13 is a divisor of 26 because 26 / 13
	has no remainder.)
	"""
	#inp = int(input("Please enter an integer: "))
	inp = 14830122 #to test execution time on larger numbers
	div = [x for x in range(2, inp) if (inp % x) == 0]
	print("Your divisors are:\n" + str(div))

def exer3():
	"""
	Take a list, say for example this one:

  	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	and write a program that prints out all the elements of the list that are less than 5.

	Extras:
		Instead of printing the elements one by one, make a new list that has all the elements
		less than 5 from this list in it and print out this new list.
		Write this in one line of Python.
		Ask the user for a number and return a list that contains only elements from the
		original list a that are smaller than that number given by the user.
	"""
	inp = int(input("Please enter a number: "))
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [x for x in a if x < inp]
	print("The following numbers are lower than the one privided\n" +str(b))
	
def exer2():
	"""
	Ask the user for a number. Depending on whether the number is even or odd, print
	out an appropriate message to the user. Hint: how does an even / odd number react
	differently when divided by 2?

	Extras:
		If the number is a multiple of 4, print out a different message.

		Ask the user for two numbers: one number to check (call it num) and
		one number to divide by (check). If check divides evenly into num, tell that
		to the user. If not, print a different appropriate message.
	"""
	inp = int(input("Please give me a number: "))
	if (inp % 4) == 0:
		print("Your number is a multiple of 4... sneaky.")
	elif (inp % 2) == 0:
		print("Your number is a multiple of 2.")
	else:
		print("Your number was not a multiple of 2.")

	inp = input("Excellent. Now give me two seperate numbers: ")
	a, b = int(inp.split()[0]), int(inp.split()[1])
	if(a%b)==0:
		print("Your first number is cleanly divisible by your second number.")
	else:
		print("Your first number was not cleanly divisible by the second number.")


def exer1():
	"""
	Create a program that asks the user to enter their name and their age.
	Print out a message addressed to them that tells them the year that they will
	turn 100 years old.

	Extras:
		Add on to the previous program by asking the user for another number and printing out
		that many copies of the previous message. (Hint: order of operations exists in Python)

		Print out that many copies of the previous message on separate lines.
		(Hint: the string "\n is the same as pressing the ENTER button)
	"""
	inp = input("Please give me your first name and age: ")
	name, age = inp.split()[0], int(inp.split()[1])
	if(age > 100):
		print("You are already 100... wow.")
		return
	year = dt.datetime.now().year + (100 - age) #Not 100% accurate though; doesn't take 
												#months/days into consideration
	print("Well "+name+", you will celebrate your 100th birthday in the year "+str(year)+"!")



#So, this works by saying that everything in this 'if' statement is ONLY run when the module
#is loaded as the primary file, rather than an imported file
if __name__ == "__main__":
	#now = datetime.datetime.now
	#before = now()
	print("Program took %f seconds" %(timeit.timeit("run()","from __main__ import run", number=1)))
	#print("Script execution time: " + str((now() - before)))