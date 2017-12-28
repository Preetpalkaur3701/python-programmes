# Here a1 is empty matrix which works as a list in below function.
print "Enter the values of first matrix"
a1 = []

for i in range(3):
	a1.append([])
	for j in range(3):
		k = input()		
		a1[i].append(k)		
# Above append is used to repeat function again and again untill we get the answer.
print a1
a2 = []

for i in range(3):
	a2.append([])
	for j in range(3):	
		a2[i].append(a1[j][i])	
	
for c in a2:
	print c


