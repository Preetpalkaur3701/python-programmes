def print_factors(x):
	for i in range (1,x+1) :
		if x % i == 0 :
			print (i)
num1 = input ("Enter first number")
print "the factors of ",num1, "is",print_factors(num1)
