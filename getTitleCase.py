
# Map the lowercase letters to uppercase letters.

def getTitleCase(text):
    
    titledText = ""

    ## Check first letter of string text
    for i in range(len(text)):
        if i == 0:
            titledText += text[i].upper()

        elif text[i].isalpha() and not text[i - 1].isalpha():
            titledText += text[i].upper()
        else:
            titledText += text[i].lower()


    return titledText
        

print(getTitleCase("moons spoons and toons"))

assert getTitleCase('Hello, world!') == 'Hello, World!'
assert getTitleCase('HELLO') == 'Hello'
assert getTitleCase('hello') == 'Hello'
assert getTitleCase('hElLo') == 'Hello'
assert getTitleCase('') == ''
assert getTitleCase('abc123xyz') == 'Abc123Xyz'
assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'
assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'
import random
random.seed(42)
chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')
for i in range(1000):
    random.shuffle(chars)
    assert getTitleCase(''.join(chars)) == ''.join(chars).title()