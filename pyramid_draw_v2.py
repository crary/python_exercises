

def drawPyramid(height):
    for rowNumber in range(height):
        leftSideSpace = '.' * (height - (rowNumber + 1))
        pyramidRow = '#' * (rowNumber * 2 + 1)

        print(leftSideSpace + pyramidRow)

drawPyramid(50)
