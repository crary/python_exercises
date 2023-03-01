## Exercise 28, border drawing

def drawBorder(width, height):
    if height <= 2 or width <= 2:
        return print("Width or Height must be above 2")
    print('+' + (width-2)*'-' + '+')
    for _ in range(height-2):
        print('|' + (width-2)*' ' + '|')
    print('+' + (width-2)*'-' + '+')   


drawBorder(5, 3)