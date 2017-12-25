
print "Hi"
print "Here you can check whether your number is armstrong or not"
def armstrong ( x , y , z ):
   		c = x*x*x + y*y*y + z*z*z
    		return c

x = input("Enter first digit")
y = input ("Enter seconf digit")
z = input ("Enter third digit")
num = armstrong( x , y , z)

#print ("armstrong"+str(armstrong(x,y,z)))
print type(num)
print type(str(x)+ str(y)+str(z))
if num > 0:
	if num == int(str(x)+ str(y)+str(z)):
		print " this is armstrong number"
	else:
		print "this is not armstrong number"
else :
	print "this is not armstrong number"

