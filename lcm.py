#LCM (least common factor)
def lcm ( x , y ):
# x > y lcm can never be negative so take atleast one value to be greater then another
	if x > y:
		greater = x
	else:
		greater = y

	if ((greater % x == 0) and (greater % y == 0)):
		lcm = greater
		return lcm
# x and y are the inputs given by the user
num1 = input("Enter first number")
num2 = input("Enter second number")
print "The LCM of ", num1, " and " ,num2, "is",lcm(num1 , num2)
