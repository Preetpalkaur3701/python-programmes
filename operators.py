# Taking the inputs from the user.

meal_cost = float(input("Enter the value"))
tip_percent = int(input("Enter the value"))
tax_percent = int(input("Enter the value"))

# Expression to find tip,tax and total cost.

tip = meal_cost * tip_percent/100
tax = meal_cost * tax_percent/100
totalcost = meal_cost + tip + tax
print (totalcost)



