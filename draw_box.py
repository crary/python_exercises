## Exercise 30, draw a box
#import border_drawing


size = 3

## Print top 2x lines of box
print( "." * (size + 1) + "+" + "-"*(size *2) + "+")
print( "." * size + "/" + "-" * (size *2) + "/|")

## Print top half of box
for row in range(size - 1):
    leftSide = "." * ((size - 1) - row)
    middle = "/" + "-" * (int(size *2) - 0) + "/"# + "."*(size + 1)  + "|"
    end = "."*(row + 1)  + "|"

    print(leftSide + middle + end)

## Print middle seam
print( "+" + "+"*int(size *2) + "+" + "-" * size + "+")

## Print bottom half of box
for rows in range(size):
    middle = "+" + "-" * ((size *2) - 0) + "+"
    rightSide = "." * ((size - 1) - rows) + "/"

    print(middle  + rightSide)
