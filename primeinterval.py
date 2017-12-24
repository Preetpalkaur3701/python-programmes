

lower = input("first number")
upper= input("secong number")
check=False
print ("prime numbersbetween",lower, "and",upper, "are:")
for num in range(lower, upper+1):
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				check=True

	if check == False:
		print num
	check=False

"""	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				break
	else:
		print (num)	"""
