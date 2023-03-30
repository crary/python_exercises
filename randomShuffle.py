import random

randomList = []

def shuffleList(value):
    global randomList
    for i in range(1, value + 1, 1):
        randomList.append(i) 

    tempList = random.sample(randomList, value)
        
    for i in range(value):
        randomList[i] = tempList[i]
    
    print(randomList)
    print(sorted(randomList))




shuffleList(20)