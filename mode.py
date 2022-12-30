from random import randint as randy

numbers = []
num_list = input("How many numbers?")

for _ in range(int(num_list)):
    numbers.append(randy(1,100))

print(numbers)

def mode(numbers):
    if len(numbers) == []:
        return None
    number_count = {}
    mostFreqnum = None
    mostFreqnumCount = 0

    for number in numbers:
        if number not in number_count:
            number_count[number] = 0 
        number_count[number] += 1
        if number_count[number] > mostFreqnumCount:
            mostFreqnum = number
            mostFreqnumCount = number_count[number]
    return mostFreqnum

print(mode(numbers))