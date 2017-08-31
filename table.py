# This programe is used to make any table upto any range you want !


print "Hello!"
# where n is an input given by the user .
n = input("please enter any number which you want to create table: ")

# palo refers to the range of your the table.
palo = input("enter range: ")

# ambbu refers to the multiples of your table.
ambu = input("enter range: ")
for i in range( palo , ambu):
	print str(n)+" X "+str(i)+" = "+str(i*n)

	
