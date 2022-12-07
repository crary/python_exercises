from cgitb import small
from random import randint, random

## Create file for random number if not already existing
number = []

## Fill file with random numbers
for _ in range(10):
    number.append(randint(0,100))

print(number)

def getsmallest():
    smallest = number[0]
    for i in number:
        if i < smallest:
            smallest = i
    return smallest

def getbiggest():
    biggest = number[0]
    for i in number:
        if i > biggest:
            biggest = i
    return biggest

print(getsmallest())
print(getbiggest())