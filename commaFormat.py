

def commaFormat(number):

    ## Convert integer number to string
    number = str(number)

    if '.' in number:
        ## Takes everything after dot
        dotPart = number[number.index('.'):]
        ## Takes everything before dot
        number = number[:number.index('.')]
    else:
        dotPart = ''


    triplet = ''
    commaNumber = ''

    ## Loop over digits from right to left
    for i in range(len(number)-1, -1, -1):
        triplet = number[i] + triplet
        
        ## When number reaches 3x length add comma
        if len(triplet) == 3:
            commaNumber = ',' + triplet + commaNumber
            triplet = ''



    # If the triplet has any digits left over, add it with a comma
    # to the comma-formatted string:
    if triplet != '':
        commaNumber = triplet + commaNumber

    return commaNumber + dotPart

print(commaFormat(66000998786.9897))