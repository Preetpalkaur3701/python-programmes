# Arrays
# The first line contains an integer, n(the size of our array).
#The second line contains n space-separated integers describing array 's elements.


data = []
n = int(raw_input('Enter how many elements you want: '))
for i in range(0, n):
    x = raw_input('Enter the numbers into the array: ')
    data.append(x)
a = (list(reversed(data)))
print ' '.join([str(x) for x in a])
