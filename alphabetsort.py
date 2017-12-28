print "Here you can sort your alphabets."
print "Start and End your sentence by quotation mark."
sen = input("Enter alphabets:")
# First we change our string into list by using .split()
alphabets = sen.split()
# Second we sort our words by using .sort()
alphabets.sort()

for alphabet in alphabets:
	print (alphabet)
