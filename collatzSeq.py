
startNum = input("Starting Number: ")
startNum = int(startNum)

def collatz():
    seq = []
    print(startNum)
    print((type(startNum)))
    seq.append(startNum)

    if startNum <= 1:
        print(f"Number is: {startNum}, exiting.")
        exit
    elif startNum % 2 == 0:
        collatz = 0
        while collatz != 8:
            collatz = startNum / 2
            seq.append(int(collatz))
            if collatz % 2 == 0:
                collatz = collatz / 2
            elif collatz % 2 != 0:
                collatz = (3 * collatz) + 1
                seq.append(collatz)
                if collatz % 2 == 0:
                    collatz = collatz / 2
                    seq.append(collatz)

    print(seq)

collatz()


# xx = 11 % 2

# print(xx)