
numberOFCoffees = input("How many coffees? ")
pricePerCoffee = input("pricePerCoffee? ")

#change input to intergers
numberOFCoffees = int(numberOFCoffees)
pricePerCoffee = int(pricePerCoffee)

def getCostOfCoffe(numberOFCoffees,pricePerCoffee):
    totalCoffeeCost = 0 
    cupsUntilFreeCoffee = 8 
    while numberOFCoffees > 0:
        numberOFCoffees -= 1
        if cupsUntilFreeCoffee == 0:
            cupsUntilFreeCoffee = 8
        else:
            totalCoffeeCost += pricePerCoffee
            cupsUntilFreeCoffee -= 1
    return totalCoffeeCost

print(getCostOfCoffe(numberOFCoffees,pricePerCoffee))
