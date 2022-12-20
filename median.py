from random import randint as randy
import random
import re

list_num = input("How many numbers in your list?")
numbers = []

for _ in range(int(list_num)):
    numbers.append(random.randint(1,50))

print(f"{numbers}\n")


def median():
    if len(numbers) == []:
        return None
    numbers.sort()
    middleIndex = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[middleIndex] + numbers[middleIndex - 1]) / 2
    else:
        return numbers[middleIndex]

print(median())
