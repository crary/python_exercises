from random import choice, randint, shuffle
import random
import string

# crate strings for each type of character
lower_Letters = string.ascii_lowercase
upper_Letters = string.ascii_uppercase
numbers = string.digits
specials = string.punctuation

# combine all character stings into single string
allCharacters = lower_Letters + upper_Letters + numbers + specials

def generatePassword(length):
    if length < 12:
        length = 12
    # create empty password list with single character from each category
    password = []
    password.append(lower_Letters[random.randint(0,25)])
    password.append(upper_Letters[ random.randint(0,25)])
    password.append(numbers[ random.randint(0,10)])
    password.append(specials[ random.randint(0,14)])

    while len(password) < length:
        password.append(allCharacters[random.randint(0,74)])

    random.shuffle(password)
    return ''.join(password)

    

print(generatePassword(20))