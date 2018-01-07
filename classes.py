import datetime

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

class MITPerson(Person):
	nextIdNum = 0
	def __init__(self,name):
		Person.__init__(self,name)
		self.idNum = MITPerson.nextIdNum
		MITPerson.nextIdNum += 1
	def getIdNum(self):
		return self.idNum
	def __lt__(self, other):
		return self.idNum < other.idNum


class Student(MITPerson):
	pass
class UG(Student):
	def __init__(self, name, classYear):
		MITPerson.__init__(self, name)
		self.year = classYear
	def getClass(self):
		return self.year
class Grad(Student):
	pass
class Grades(object):
	def __init__(self):
		self.students = []
		self.grades = {}
		self.isSorted = True
	def addStudent(self, student):
		if student in self.students:
			raise ValueError('Duplicate Student')
		self.students.append(student)
		self.grades[student.getIdNum()] = []
		self.isSorted = False
	def addGrade(self, student, grade):
		try:
			self.grades[student.getIdNum()].append(grade)
		except:
			raise ValueError('Student not in mapping')
	def getGrades(self, student):
		try:
			return self.grades[student.getIdNum()][:] #returns a copy of the list
		except:
			raise ValueError('Student not in mapping')
	def getStudents(self):
		if not self.isSorted:
			self.students.sort()
			self.isSorted = True
		#return self.students[:]  #returns a copy of the list
		for s in self.students:
			yield s
