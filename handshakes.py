

people = ['Alice', 'Bob', 'David', 'Rix', 'Jilfy', 'Vince', 'Ross', 'Valeri']

def printHandShakes(people):
    
    numberOfhandhakes = 0

    for i in range(0, len(people) - 1):
        for j in range(i + 1, len(people)):
            print(people[i], " shakes hands with ", people[j])
            numberOfhandhakes += 1
    return print(numberOfhandhakes)

printHandShakes(people)

