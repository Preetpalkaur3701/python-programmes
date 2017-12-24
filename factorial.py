
def  recur_factorial(n):
	if n == 1 :
		return n
	else:
		 return n * recur_factorial(n-1) 

n = input("Enter the number")

#for i in range (1, n+1):
#	factorial = n*i
print "The factorial of " , n , "is" , recur_factorial(n)
