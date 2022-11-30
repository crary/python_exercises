## Exercise 8 Python Programming Gently Explained
filename = "greet.txt"

def writeToFile(filename, text):
    with open(filename, "w") as myfile:
        myfile.write(text)
        myfile.close()

def appendToFile(filename, text):
    with open(filename, "a") as myfile:
        myfile.write(text)
        myfile.close()

def readFromFile():
    with open(filename) as myfile:
        if myfile.read() == "Hello\nGoodbye\n":
            print ("Contents Correct")
        else:
            print("Content Error")

writeToFile(filename, "Hello\n")
appendToFile(filename, "Goodbye\n")
readFromFile()