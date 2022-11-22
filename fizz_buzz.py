
import string


number = input("Enter number: ")
number = int(number)

    
def fizz_buzz(number):
        if (number % 3 == 0) and (number % 5 == 0):
           return print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            return print("Fizz", end=" ")
        elif number % 5 == 0:
            return print("Buzz", end=" ")
        else:
            print (number, end=" ")


#fizz_buzz(number)
for i in range(1, number+1):
    fizz_buzz((i))
    