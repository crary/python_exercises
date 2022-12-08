from math import prod as prod
import random

num_list = []
numbers = []

for _ in range(10):
    num_list.append(random.randint(1,10))

for _ in range(5):
    numbers.append(random.randint(1,5))

print(num_list)
print(len(num_list))

def calc_sum():
    if num_list == []:
        return None
    return sum(num_list, 0)

def calc_product():
    return prod(num_list)

def calculateSum(mylist):
    result = 0
    for i in mylist:
        result += i
    return result

def calculateProduct(mylist):
    result = 1
    for i in mylist:
        result = result * i
    return result
    
print("Sum total is",calc_sum())
print("Product total is",calc_product())

print(numbers)
print("Second sum method result:", calculateSum(numbers))
print("Second product method result:", calculateProduct(numbers))