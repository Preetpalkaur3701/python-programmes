print "Welcome ! Here you can convert kilometers to miles"
print "one kilometer = 0.621371miles "
num = 0.621371
def conversion(x , num):
	c = x * num
	return c
x = input("Enter the numberin kilometers")
if x == 0:
	print "your answer is zero"
if x > 0:
	print ("miles"+str(conversion(x , num)))
