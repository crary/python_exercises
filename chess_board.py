while True:
    try:
        column = input("Enter Column Number: ")
        if int(column) > 7:
            raise ValueError
        break
    except ValueError:
        print("Column value must be 0 - 7")

while True:
    try:
        row = input("Enter row Number: ")
        if int(row) > 7:
            raise ValueError
        break
    except ValueError:
        print("Row value must be 0 - 7")

def getChessSquareColor(column, row):
    if (int(column) % 2 == 0 and int(row) % 2 == 0) or (int(column) == 1 and int(row) == 1):
        return str("white")
    elif (int(column) % 2 == 1 or int(row) % 2 == 1):
        return str("black")

print(getChessSquareColor(column, row))

assert getChessSquareColor(1, 1) == "white"
assert getChessSquareColor(0, 0) == "white"
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
