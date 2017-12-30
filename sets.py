def insertToSet(no):
	s = set()
	for i in range(no):
		s.add(input())
	return s
# In the above function we have an empty set in which our input stores. .add is also same like .append .

n1=input()

a = insertToSet(n1)
# n1 is the number of possible inputs given by user.
print a

n2 = input()

b = insertToSet(n2)
print b

print a|b
print a & b
print a - b
print a ^ b

"""def insertValuetoSet():
	t=set()
	item = raw_input()
	while item != "None":
		t.add(item)
		item = raw_input()
	return t
# This is second method raw_input means that the input provided by the user is in string form.

a = insertValuetoSet()
print a

for i in range(n1):
	a.add(input())

print a

n2=input()
b=set()
for i in range(n2):
	b.add(input())

print b

print a|b"""
