totalSec = input("Enter seconds: ")
totalSec = int(totalSec)

   
def getHoursMinutesSeconds(totalSec):
    if totalSec == 0:
        return print(str("0s"))

    hours = 0
    while totalSec >= 3600:
        hours += 1
        totalSec -= 3600
        
    minutes = 0 
    while totalSec >= 60:
        minutes += 1
        totalSec -= 60
    
    seconds = totalSec
    hms = []
    
    if hours > 0:
        hms.append(str(hours)+'h')
    if minutes > 0:
        hms.append(str(minutes)+'m')
    if seconds > 0:
        hms.append(str(minutes)+"s")

    return ' '.join(hms)

print(getHoursMinutesSeconds(totalSec))
