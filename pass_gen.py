from random import choice, randint, shuffle
import random
import string

length = 14
#integers=[]
#letters=[]

def numGen(length):
    # Generate random string of numbers
    global randomNumbers
    numbers = string.digits
    randomNumbers = ''.join(random.choice(numbers) for x in range(length))
    return randomNumbers

def letterGen(length):
    # Generate random string of Letters
    global randomLetters
    Letters = string.ascii_letters
    randomLetters = ''.join(random.choice(Letters) for i in range(length))
    return randomLetters

def symGen(length):
    # Generate random symbols
    global randomSym
    symbols = string.punctuation
    randomSym = ''.join(random.choice(symbols) for i in range(length))
    return randomSym
   
def passGen():
    # Create Full string of all characters and symbols and shuffle
    allChar = randomSym + randomNumbers + randomLetters
    allChar = list(allChar)
    random.shuffle(allChar)
    allChar = ''.join(allChar)
    # Slice string down to 14 characters
    passSlice = slice(0,-1,3)
    allChar = allChar[passSlice]

    return allChar

letterGen(length)
numGen(length)
symGen(length)

print(passGen())