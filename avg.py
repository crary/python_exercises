from random import randint as rint

numbers = []

for _ in range(10):
    numbers.append(rint(1,1000))

print(numbers)
denom = len(numbers)

def average(mylist):
    if len(numbers) == 0:
        return None
    tnum = 0
    for i in mylist:
        tnum += i
    return tnum / denom


print("List average is:",average(numbers))
