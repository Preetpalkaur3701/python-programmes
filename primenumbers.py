print "Hello!"
print "Here you can find whether your given nuber is prime number or not !"
n = input("Enter any number")
check=False
if n > 1:
	for i in range(2,n):
		if (n % i) == 0:
			check=True

if check:
	print "your number is not prime number"
else:
	print "your number is  prime number"
