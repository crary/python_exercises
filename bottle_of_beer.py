import time

global bottles
bottles = 99

def beerBottle(bottles):
    while bottles != 0:
        print(f"{bottles} bottles of beer on the wall,")
        time.sleep(1)
        print(f"{bottles} bottles of beer,")
        time.sleep(1)
        print("Take one down, pass it around,")
        time.sleep(1)
        bottles -= 1
        print(f"{bottles} bottles of beer on the wall,")
        print("\n")
        time.sleep(2)
    return bottles

beerBottle(bottles)



