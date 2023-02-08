
year = input("Enter year: ")


def isLeapYear(year):

    if int(year) % 400 == 0:
        print("Leap year.")
    elif int(year) % 100 == 0:
        print("NOT leap year")
    elif int(year) % 4 == 0:
        print("This is a leap year")
    else:
        print("NOT Leap year")
        
isLeapYear(year)


