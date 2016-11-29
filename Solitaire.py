
import json
import sys
import random

class Solitaire:
	def __init__(self, idioms, mode):
		'''
		idioms : all the idioms to be indexed
		mode : 0 pinyin, 1 character
		'''
		self.idioms = idioms
		self.used = []
		self.mode = mode

	def inIdioms(self, idiom):
		for idm in self.idioms:
			if idm.idiom == idiom:
				return idm
		return null

	def nextIdiom(self, idiom):
		idm = self.inIdioms(idiom)

		if idm is None:
			print("Not a idiom to me, choose your words wisely.")
		else:
			for obj in self.idioms:
				if self.mode == 0 and obj.firstpy == idm.lastpy and obj not in self.used:
					self.used.append(obj)
					return obj

				if self.mode == 1 and obj.idiom[0] == idm.idiom[-1] and obj not in self.used:
					self.used.append(obj)
					return obj

	def clearUsedList(self):
		self.used = []

class ChengYu:
	def __str__(self):
		return self.idiom + " " + self.pinyin + " " + self.explanation

	def __init__(self, idiom, pinyin, explanation, source, example, spinyin):
		self.idiom = idiom
		self.pinyin = pinyin
		self.explanation = explanation
		self.source = source
		self.example = example
		self.spinyin = spinyin
		self.firstpy = ""
		self.lastpy = ""

		if self.pinyin != "":
			self.lastpy = self.pinyin.split(' ')[-1]
			self.firstpy = self.pinyin.split(' ')[0]

	@classmethod
	def fromJson(cls, obj):
		idiom = obj['chengyu']
		pinyin = obj['pinyin']
		explanation = obj['diangu']
		source = obj['chuchu']
		example = obj['lizi']
		spinyin = obj['spinyin']

		t = cls(idiom, pinyin, explanation, source, example, spinyin)

		return t


if __name__=="__main__":

	json_file = "output.json"
	
	with open(json_file, encoding='utf-8') as data_file:
		usableData = json.load(data_file)

	idioms = []

	for obj in usableData:
		idiom = ChengYu.fromJson(obj)
		idioms.append(idiom)

	solitaire = Solitaire(idioms, 0)

	for i in range(0, len(idioms)):
		input_idiom = idioms[i]
		count = 1

		while True:
			try:
				#print(input_idiom)
				input_idiom = solitaire.nextIdiom(input_idiom.idiom)
				if input_idiom is None:
					break
				count = count + 1
			except Error:
				print('error')
		print(idioms[i].idiom + " " + str(count))

		solitaire.clearUsedList()
