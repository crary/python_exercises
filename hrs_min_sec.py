totalSec = input("Enter seconds: ")
hours = ''

def gethours():
    hours = int(totalSec) / 3600
    mins = (int(totalSec) % 3600) / 60
    seconds = (int(totalSec) % 3600) % 60
    #print(int(hours),str("hrs") , int(mins),str("mins") , int(seconds),str("secs") )
    print(str(int(hours)) + str("hrs") , str(int(mins)) + str("mins") , str(int(seconds)) + str("secs") )

gethours()
