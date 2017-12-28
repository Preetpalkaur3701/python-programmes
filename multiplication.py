print "Enter the values of first matrix"
a1 = []

for i in range(3):
	a1.append([])
	for j in range(3):
		k = input()		
		a1[i].append(k)		
# Above append is used to repeat function again and again untill we get the answer.
print a1
print "Enter the values of second matrix"

a2 = []

for i in range(3):
	a2.append([])
	for j in range(3):
		k = input()		
		a2[i].append(k)		

print a2
c=[]

for i in range(3):
	c.append([])
	for j in range(3):	
		c[i].append(a1[i][k] * a2[k][j])		

print c

