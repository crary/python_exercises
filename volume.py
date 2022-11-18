length = input("Length = " )
width = input("Height = ")
Height = input("Height = ")

def area (length, width):
    return int(length) * int(width)

def perimeter ():
    return int(length) + int(width) + int(length) + int(width)

def volume ():
    return int(length) * int(width) * int(Height)

def surface_area ():
    return (int(length) * int(width) * 2) + (int(length) * int(Height) * 2) + (int(Height) * int(width) * 2)


print("Area is: " + str(area(length, width)))
print("Perimeter is: " + str(perimeter()))
print("Volume is: " + str(volume()))
print("Surface area is: " + str(surface_area()))