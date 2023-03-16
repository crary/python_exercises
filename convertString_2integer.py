

def convertStringToInteger(stringNum):

    
    ## Check if iteger is Zero
    if stringNum == '0':
        return 0


     ## Create integer to string dictionary
    DIGITS_INT_TO_STR = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    if stringNum[0] == '-':
        isNegative = True
        stringNum = stringNum[1:]
    else:
        isNegative = False

    ## Integer starts at zero
    integerNum = 0


    for i in range(len(stringNum)):
        digit = DIGITS_INT_TO_STR[stringNum[i]]
        integerNum = (integerNum * 10) + digit

    if isNegative:
        return -integerNum
    else:
        return integerNum


print(convertStringToInteger('-7777789'))