import getpixel
getpixel.enable(im)
r , g , b = im.getpixel(0,0)
print "Red; %s , green; %s , Blue; %s" % (r,g,b)
pic1 = makepicture("IMG_20170419_150339.jpg")
for pixel in getpixel("pic1.jpg"):
    if pixel " Red; %s ":
       return "Green: %s"

    if pixel "Green: %s": 
       return "Blue: %s"

