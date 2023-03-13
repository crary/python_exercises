

def drawBox(size):
    ## If less then 1, draw nothing
    if size < 1:
        return

    ## Draw top
    print(' '*(size + 1) + '+' + '-'*( size *2) + '+')

    ## Draw top surface
    for i in range(size):
        print(' '*(size - i) + '/' + ' ' * (size * 2) + '/' + ' ' * i + '|')

    # Draw top line on top surface:
    print('+' + '-' * (size * 2) + '+' + ' ' * size + '+')

    # Draw front surface:
    for i in range(size - 1, -1, -1):   
        print('|' + ' ' * (size * 2) + '|' + ' ' * i + '/')

    # Draw bottom lie on front surface:
    print('+' + '-' * (size * 2) + '+')

for i in range(1, 6):
    drawBox(i)