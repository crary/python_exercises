check_num = input("Enter your number: ")

def evenOdd ( check_num ):
    if int(check_num) % 2 == 0:
        return print ( str(bool(int(check_num) % 2 == 0)) + " " + str(check_num) + " is even.")
    else:
        return print( str(bool(int(check_num) % 2 == 0)) + " " +  str(check_num) + " is odd.")

evenOdd(check_num)        
