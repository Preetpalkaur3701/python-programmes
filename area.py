import math

def area(a, b):
    c = a * b
    return c

def volume(a , b, c):
    c = a * b * c
    return c

def perimeter (a , b ):
	c = 2 * (a + b)
	return c

def area_of_circle(radius):
	c = math.pi * radius * radius
	return c
def area_of_triangle (a , b):
	c = 0.5 * a *b
	return c

def area_of_square (a):
	c = a * a
	return c

print "Type ok to go ahead !"
begin = raw_input("Here you can find the area of rectangle , volume of cuboid , perimeter of retangle , area of square  !:")

if begin == "ok":
    print "put all the values in centimeters"

    length = input("length of object: ")
    breadth = input("breadth of object: ")
    height = input("height of object: ")
    radius = input ("radius of circle:")
    base = input ("base of triangle:")
    side = input("side of square:")
    print "What you want?"
    print "1) To find the area of rectangle?"
    print "2) To find the volume of Cuboid?"
    print "3) To find the perimeter of rectangle?"
    print "4) To find the area of circle?"
    print "5) To find the area of triangle?"
    print "6) To find the area of square?"
    print "7) for all above"

    choice = raw_input("Enter 1 or 2 or 3 or 4 or 5 or 6 or 7:")

    if choice in {"1"}:
        print "area of rectangle:", area(length, breadth)
    elif choice in {"2"}:
        print "volume of cuboid:", volume(length, breadth, height)
 
    elif choice in {"3"}:
	print "perimeter of square :" , perimeter(length, breadth)

    elif choice in {"4"}:
	print "area of circle:" , area_of_circle(radius)
	
    elif choice in {"5"}:
	print "area of Triangle:" , area_of_triangle( height , base)

    elif choice in {"6"}:
		print "area_of_square:" , area_of_square(side)

	
    elif choice in {"7"}:
        print "area of rectangle:", area(length, breadth)
        print "volume of cuboid:", volume(length, breadth, height)
        print "perimeter of square:",perimeter(length, breadth)
        print "area of circle:" , area_of_circle(radius)
        print "area of Traingle:" , area_of_triangle( height , base)
        print "area of square:" , area_of_square(side)
