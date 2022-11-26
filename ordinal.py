number = input("Enter your number: ")
number = str(number)

#print(number[-3:-1])

def ordinalSuffix(number):
    ends = (number[-1])
    if number[-2:] in ("11","12","13"):
        return print(number+str("th"))
    elif ends == "1":
        return print(number+str("st"))
    elif ends == "2":
        return print(number+str("nd"))
    elif ends == "3":
        return print(number+str("rd"))
    else :
        return print(number+str("th"))


ordinalSuffix(number)