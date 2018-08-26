"""
Task
Given an integer, n, print its first 10 multiples. Each multiple n x i (where  1 <=i <= 10 ) should be printed on a new line in the form: n x i = result.

"""
n = int(input("Enter the number"))
for i in range(1,11):
	print('{0} x {1} = {2}'.format(n, i, n * i))
    
