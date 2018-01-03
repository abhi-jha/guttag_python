from classes import IntSet , Person, MITPerson, Grades, Grad, UG, Student
s = IntSet()
s.insert(3)
print s.member(3)
print s

p = Person('Aa ')
q = Person('v ')
r = Person('d ')

l = [p,q,r]
for i in l:
	print i
l.sort()
print('\n\n')
for i in l:
	print i

p1 = MITPerson('Me may')
print(str(p1) + '\'s id number is '+str(p1.getIdNum())) 

p1 = MITPerson('Mark')
p2 = MITPerson('Billy Bob')
p3 = MITPerson('Billy Bob')
p4 = Person('Billy Bob')

print 'p1 < p2 ', p1 < p2
print 'p3 < p2 ', p3 < p2
print 'p4 < p1 ', p4 < p1
#print 'p1 < p4 ', p1 < p4

def gradeReport(course):
	report=''
	for s in course.getStudents():
		tot  = 0.0
		numGrades = 0
		for g in course.getGrades(s):
			tot += g
			numGrades += 1
		try:
			average = tot/numGrades
			report = report + '\n' + str(s)+'\'s mean grade is '+ str(average)
		except ZeroDivisionError:
			report = report  + '\n'+ str(s)+' has no grades'
	return report

ug1 = UG('Jane Doe', 2014)
ug2 = UG('Jane Doe', 2015)
ug3 = UG('David Henry', 2003)

g1 = Grad('Billy Buckner')
g2 = Grad('Bucky F. Dent')

sixHundred = Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)
for s in sixHundred.getStudents():
	sixHundred.addGrade(s,75)
sixHundred.addGrade(g1,25)
sixHundred.addGrade(g2,100)
sixHundred.addStudent(ug3)
print gradeReport(sixHundred)