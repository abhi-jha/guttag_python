class IntSet(object):
	def __init__(self):
		self.vars = []
	def insert(self,e):
		if not e in self.vars:
			self.vars.append(e)
	def member(self,e):
		return e in self.vars
	def remove(self,e):
		try:
			self.vars.remove(e)
		except:
			raise ValueError(str(e)+' not found')
	def getMembers(self):
		return self.vars[:]
	def __str__(self):
		self.vars.sort()
		result = ''
		for e in self.vars:
			result = result + str(e) + ','
		return '{' + result[:-1] + '}'

import datetime

class Person(object):
	def __init__(self, name):
		self.name = name
		try:
			lastBlank = name.rindex(' ')
			self.lastName = name[lastBlank+1:]
		except:
			self.lastName = name
		self.birthday = None
	def getName(self):
		return self.name
	def getLastName(self):
		return self.lastName
	def setBrthDay(self,birthdate):
		self.birthday = birthdate
	def getAge(self):
		if self.birthday == None:
			raise ValueError
		return (datetime.date.today() - self.birthday).days
	def __lt__(self,other):
		if self.lastName == other.lastName:
			return self.name < other.name
		return self.lastName < other.lastName
	def __str__(self):
		return self.name
