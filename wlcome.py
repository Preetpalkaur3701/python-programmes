#


count = 0


print "Welcome to my Quiz"
print "\nIf you submit the correct answer then\nyou will get 5 marks and if its wrong\nanswer then 5 marks will be detected from your total\n"
print "YES or NO"
begin = raw_input("Would you like to participate in my quiz?")
if begin == "yes" :
	
	print "Grand Central Terminal, Park Avenue, New York is the world's ?"
	print "A) largest railway station"
	print "B) highest railway station"
	q1 = raw_input("Enter A or B: ")
	if q1 == "A" or q1 =="a":    		
		count += 5
		
		print "well done ! you got ir right "
	elif q1 == "B" or q1 == "b":
		print "Sorry it's the wrong answer :(\n"
		count -= 5
	
	print "Entomology studies what?"
	print "A) Behaviour of human being "
	print "b) Insects"
	q2 = raw_input("Enter A or B")
	if q2 == "B" or q2 == "b":
		count += 5

		print " Great!"
	elif q2 == "A" or q2 == "a" :
		print "Sorry it's the wrong answer :(\n"
		count -= 5

	print "who is the national bird of india?"
	print "A) Peacock"
	print "B) Eagle "
	q3 = raw_input("Enter A or B:")
	if q3 == "A" or q3 == "a":
		count += 5

		print " wow! That's Awesome"
	elif q3 == "B" or q3 == "b":
		print "Sorry it's the wrong answer :(\n"
		count -= 5
else:
	print "Thankyou and Goodbye!"
	
print "Marks: ", count
print "Quiz is over now . Thankyou for being the part of our Quiz"
