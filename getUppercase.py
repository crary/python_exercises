

# Map the lowercase letters to uppercase letters.
LOWER_TO_UPPER = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g':
'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O',
'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x':
'X', 'y': 'Y', 'z': 'Z'}

def getUppercase(text):

    upperCase = ""

    for i in text:
        if i in LOWER_TO_UPPER:
            upperCase = upperCase + LOWER_TO_UPPER[i]
        else:
            upperCase += i

    return upperCase

print(getUppercase("hEllo"))


assert getUppercase('Hello') == 'HELLO'
assert getUppercase('hello') == 'HELLO'
assert getUppercase('HELLO') == 'HELLO'
assert getUppercase('Hello, world!') == 'HELLO, WORLD!'
assert getUppercase('goodbye 123!') == 'GOODBYE 123!'
assert getUppercase('12345') == '12345'
assert getUppercase('') == ''

