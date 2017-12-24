n = input("Enter the number")

data = []

for i in range (0 , n):
	if i in {0, 1}:
		data.append(i)
	else:
		nextTerm = data[i-1] + data[i-2]
		data.append(nextTerm)

print data