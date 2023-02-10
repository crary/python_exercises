import leap_year
import datetime

## Months with only 30 days
thirty = [ 9, 4, 6, 11 ]

def checkDate(year,month,day):
        ## Check valid months
        if (month <= 0 or month >= 13):
            return False
        ## Check valid days
        elif day > 31 or day == 0:
            return False
        ## Check for months with only 30 days
        elif any( month == m for m in thirty ) and day > 30:
            return False
        ## Calculate for leap years
        if month == 2 and day == 29 and leap_year.isLeapYear(year) == False:
            return False
        else:
            return True


assert checkDate(1999, 12, 31) == True
assert checkDate(2000, 2, 29) == True
assert checkDate(2001, 2, 29) == False
assert checkDate(2029, 13, 1) == False
assert checkDate(1000000, 1, 1) == True
assert checkDate(2015, 4, 31) == False
assert checkDate(1970, 5, 99) == False
assert checkDate(1981, 0, 3) == False
assert checkDate(1666, 4, 0) == False

## Iterate through a million day through checkDate function
d = datetime.date(1970,1,1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
    assert checkDate(d.year, d.month, d.day) == True
d += oneDay

print(checkDate(2015,9,31))

