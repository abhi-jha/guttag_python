from classes import IntSet , Person

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
