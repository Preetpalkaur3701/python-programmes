import calendar
#(calendar.textcalendar),this means that we want written calendar where as calendar sunday means that we want our calendar to start from sunday. 
c = calendar.TextCalendar(calendar.SUNDAY)
# we can change the year and month as we want by giving required information.
year = input("Enter the year")
month = input("Enter the month") 
str= c.formatmonth(year,month)
print str
