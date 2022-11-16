
celsius= input( "Enter Celsius: ")
 
# f = int(celsius) * 9/5 + 32
# print(f)

def convertToFahrenheit (celsius):
    return int(celsius) * (9 / 5) + 32

print(round(convertToFahrenheit(celsius), 3))

## assert statements stop the program if their condition is False
assert convertToFahrenheit(100) == 212
assert convertToFahrenheit(0) == 32
