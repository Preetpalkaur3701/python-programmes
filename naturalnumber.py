print "Hi ! Here you can find the sum of natural numbers"
print "Please enter only positive numbers , negative numbers are not included in natural numbers"
#in next line the function is used which gives a path to the programme by which the we can get the sum of numbers.  
def sum(a,b):
	c= a+b
	return c
#here a and b are the inputs taken from user.
a = input("Enter first number")
b = input("Enter second number")
print ("sum"+str(sum(a,b)))
#sum >0 is written here because natural numbers are always positive.
if sum > 0 :
	print "the sum of your is natural number"


