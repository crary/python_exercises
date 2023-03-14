## Exercise 31: Convert integers to strings

def convertIntToString(integerNum):
    ## Check if iteger is Zero
    if integerNum == 0:
        return '0'
    
    ## Create integer to string dictionary
    DIGITS_INT_TO_STR = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    ## Check if integer is negative
    if integerNum < 0:
        isNegative = True
        integerNum = -integerNum
    else:
        isNegative = False

    ## Create empty string
    stringNum = ""

    while integerNum > 0:
        onesPlace = integerNum % 10
        stringNum = DIGITS_INT_TO_STR[onesPlace] + stringNum
        integerNum //= 10


    if isNegative:
        return '-' + stringNum
    else:
        return stringNum
 

print(convertIntToString(1995))

for i in range(-10000, 10000):
    assert convertIntToString(i) == str(i)