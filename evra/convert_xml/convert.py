import json
from bs4 import BeautifulSoup
import os


dir_path = os.path.dirname(os.path.realpath(__file__))


def debug_save(s):
	"""Takes a string and saves it to debug.txt.
	   Really only used for taking data and giving it to me outside of runtime"""
	with open(os.path.join(dir_path, 'debug.txt'), 'w') as out:
		out.write(s)

#I did have to convert some <text /> legendary entries before running this
def convert_beastiary():
	"""converts the raw xml file from dropbox into usable json"""
	with open(os.path.join(dir_path, 'xml/beastiary.xml'), 'rb') as f:
		soup = BeautifulSoup(f, 'lxml')
		print('Beastiary~~Finished loading file.')

	m = dict()

	for monster in soup.compendium.find_all('monster'):
		#init and name entry
		big = dict() 
		x = monster.findChild('name', recursive=False).contents[0]

		#loop through each entry in monster
		for child in monster.findChildren(recursive=False):
			#skip name entry since already obtained
			if (child.contents):
				if(child.name == 'name'):
					continue

			#does the entry have sub-entries?
			if child.findChild('name'):
				#creates the name for big
				if not (child.name + 's') in big.keys():
					big[child.name + 's'] = dict()
				
				#names mini
				n = child.findChild('name').contents[0]
				mini = dict()

				for c in child.findChildren(recursive=False):
					if(c.contents):
						if c.name == 'name':
							continue

						if c.name in mini.keys():
							mini[c.name] += '\n' + c.contents[0]
						else:
							mini[c.name] = c.contents[0]
				#add everything to big
				big.get(child.name + 's')[n] = mini

			if(child.contents):
				big[child.name] = child.contents[0]
		m[x] = big


	print('Beastiary~~Finished converting file')
	with open(os.path.join(dir_path, 'json/beastiary.json'), 'w') as out:
		json.dump(m, out, indent=4)
	print('Beastiary~~Finished saving')

def patch_beastiary():
	"""applies patches to fix shit in the converted json file"""
	with open(os.path.join(dir_path, 'json/beastiary.json'), 'r') as f:
		data = json.load(f)
	print('Beastiary~~File loaded for patching')
	
	for key, val in data.items():
		#Convert size to human readable
		if 'size' in val.keys():
			x = val['size']
			if x == 'T': x = 'Tiny'
			elif x == 'S': x = 'Small'
			elif x == 'M': x = 'Medium'
			elif x == 'L': x = 'Large'
			elif x == 'H': x = 'Huge'
			elif x == 'G': x = 'Gargantuan'
			val['size'] = x

		#Turn language string into list
		if 'languages' in val.keys():
			val['languages'] = val['languages'].split(',')

		#Convert hp into hit dice and hp pairs
		if 'hp' in val.keys():
			if not val['hp'] == '0':
				hp, dice = val['hp'].split('(')
				dice = dice.replace(')', '')
				val['hp'] = hp.strip()
				val['hit dice'] = dice.strip()
			else:
				val['hit dice'] = '0d0'
		
		#Convert types into list
		if 'type' in val.keys():
			# #need to find possible types first
			# l = set()
			# for kor, kal in data.items():
			# 	l |= set(kal['type'].split(','))
			# s = ''
			# for i in l:
			# 	s += i + '\n'
			# debug_save(s)
			# exit()
			old = val['type'].split(',')
			new = list()
			for i in old:
				if "Volo\'s" in i: 
					val['source'] = "Volo\'s Guide: XXX"
					continue
				elif "monster man" in i: 
					val['source'] = "Monster Manual: XXX"
					continue
				elif "out of the" in i: 
					val['source'] = "Out of the Abyss: XXX"
					continue
				elif "of strahd" in i: 
					val['source'] = "Curse of Strahd: XXX"
					continue
				elif "storm king" in i: 
					val['source'] = "Storm King\'s Thunder: XXX"
					continue
				elif "tal evil" in i: 
					val['source'] = "Elemental Evil: XXX"
					continue
				elif "of dragons" in i: 
					val['source'] = "Tyranny of Dragons: XXX"
					continue
				elif "lost mine" in i: 
					val['source'] = "Lost Mine of Phandelver: XXX"
					continue
				new += i.strip().split('(')
			old = list()
			for i in new:
				old.append(i.strip().replace(')', ''))
			val['type'] = old

		#Remove action/trait/reaction/legendary "/n" lines
		if True:
			if val.get('legendary') == '\n': del val['legendary']
			if val.get('action') == '\n': del val['action']
			if val.get('reaction') == '\n': del val['reaction']
			if val.get('trait') == '\n': del val['trait']

		#Fix attack actions

		# print(data[key])
		# break
		data[key] = val
	
	print('Beastiary~~Done patching data')
	#now output the data back into the file
	with open(os.path.join(dir_path, 'json/beastiary.json'), 'w') as out:
		json.dump(data, out, indent=2)
	print('Beastiary~~Wrote patches to file')


#Run the functions
convert_beastiary()
patch_beastiary()
exit()
