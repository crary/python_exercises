numberOfCoffees = input("Enter number of coffees: ")
pricePerCoffee = input("Enter price per coffee: ")

#Change input to integers
numberOfCoffees = int(numberOfCoffees)
pricePerCoffee = int(float(pricePerCoffee))

def getCostOfCoffee(numberOfCoffees,pricePerCoffee):
    freeCoffees =  numberOfCoffees // 9
    totalCost = numberOfCoffees * pricePerCoffee
    totalCost -= freeCoffees
    return totalCost

print(getCostOfCoffee(numberOfCoffees,pricePerCoffee))
