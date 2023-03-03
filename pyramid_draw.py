from distutils.command.build import build

def pyrmidDraw(height):
    if height <= 0:
        return print("Height can't be zero")

    if height > 4:
        row = 4
    else: 
        row = height

    buffer = 0
    ## print the top of the pyramid
    print( str(' ')*row + (height-(height-1))*'#' )

    if height >= 4:
        for _ in range(height):
            height -= 1
            row -= 1
            buffer += 2
            print( str(' ')*(row) + (height-(height-1))*'#' + '#'*buffer, end='\n' )

pyrmidDraw(5)