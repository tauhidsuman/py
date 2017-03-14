#!/usr/bin/python
"""
Create a class and fill the class with arbitrary information.
Iterate through a loop and create X number of objects.
Then search through the array of X objects to find Y.
Record time.
"""
import datetime
import time
import threading

class Obj:
	name = ""
	val = 0

	def __init__(self, n, v):
		self.name = n
		self.val = v

	def eq(self, v):
		return bool(self.val == v)

class first(threading.Thread):
	def run(self):
		list = []
		for i in range(100000):
			list.append(Obj("FObject " + str(i), i))
		for x in list:
			if(x.eq(98080)):
				print("Found object: ",x.name)
			break

class second(threading.Thread):
	def run(self):
		list = []
		for i in range(100000):
			list.append(Obj("SObject " + str(i), i))
		for x in list:
			if(x.eq(98080)):
				print("Found object: ",x.name)
			break

before = datetime.datetime.now()

f, s = first(), second()
f.start()
s.start()

while True:
	if(f.isAlive() == False) and (s.isAlive() == False):
		print(str(datetime.datetime.now() - before))
		break



