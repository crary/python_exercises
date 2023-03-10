## Exercise 30, draw a box
#import border_drawing

size = 5


print( "." * (int(size) + 1) + "+" + "-"*int(size *2) + "+")
print( "." * (int(size)) + "/" + "-" * (int(size *2) - 0) + "/|")

for row in range(size - 1):
    leftSide = "." * ((size - 1) - row)
    middle = "/" + "-" * (int(size *2) - 0) + "/"# + "."*(size + 1)  + "|"
    end = "."*(row + 1)  + "|"



    print(leftSide + middle + end)
