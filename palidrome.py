# palidrome means the word is same in forward as well as in backward direction.
print "Hi! Here you can check your string whether your string is palidrome or not"
print "Before writing the string start and end with colons."

a = input('write any word in forward direction:')
rev_str = reversed(a)
if list(a) == list(rev_str):
	print "String is Palidrome"
else :
	print "Please Try again"
