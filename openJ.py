#!/usr/bin/python
import json
import time
import datetime

before = datetime.datetime.now()

class Data:
	db = dict()

	def __init__(self):
		if not self.db:
			with open('json/spells.json') as x:
				self.db['spells'] = json.load(x)


	def find_spell(self, name):
		results = []
		for key, val in self.db['spells'].items():
			if key == 'query': continue
			if name.lower() in val['name'].lower():
				results.append(val)
		return results
				

for x in Data().find_spell("fire"):
	print(x['name'])


print("Script duration: " + str(datetime.datetime.now() - before))
		
