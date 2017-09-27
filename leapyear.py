print "Here you can finder whether year is leap year or not"

year = input("Enter any year")
if (year % 4) == 0 :
	if (year % 100) == 0:
		if (year % 400) == 0:
			print ("{0}this is leap year".format(year))
		else:
			print ("{0}this is not leap year".format(year))
	else:
		print("{0}this is leap year".format(year))
else:
	print ("{0}this is not leap year".format(year))
