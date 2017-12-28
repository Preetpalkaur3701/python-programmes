print "Here you can sort your words alphabetically."
print "Start and End your sentence by quotation mark."

sen = input("write the sentence:")
# First we change our string into list by using .split()
words = sen.split()
# Second we sort our words by using .sort()
words.sort()

for word in words:
	print (word)
