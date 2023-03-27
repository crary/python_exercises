


def makeChange(amount):
    ## Create change dictionary
    change = {}

    ## Get change for quarters
    quarter = amount // 25
    if quarter > 0:
        change['quarters'] = quarter
    else:
        pass

    amount -= 25 * quarter
    ## Get changer for dimes
    dime = amount // 10
    if dime > 0:
        change['dimes'] = dime
    else:
        pass

    amount -= 10 * dime
    ## Get change for nickel
    nickel = amount // 5
    if nickel > 0:
        change['nickels'] = nickel
    else:
        pass

    amount -= 5 * nickel
    ## Get change for pennies
    penny = amount
    if penny > 0:
        change['penny'] = penny
    else:
        pass

    #amount -=  penny

    return change



assert makeChange(30) == {'quarters': 1, 'nickels': 1}
assert makeChange(10) == {'dimes': 1}
assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'penny': 2}
assert makeChange(100) == {'quarters': 4}
assert makeChange(125) == {'quarters': 5}




