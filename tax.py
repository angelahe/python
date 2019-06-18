#############################################
#
# tax function
# use hardcoded input
# create tests first
# copy and reuse as much code as possible
#
##############################################
from math import floor

def round_it(num):

    whole = floor(num)
    part = num - whole
    if part >= 0.5:
        result = whole + 1
    else:
        result = whole
    
    return result

def calc_tax(income=0):

    brackets = [(0, 0),
        (47630, 15),
        (95259, 20.5),
        (147667, 26),
        (210371, 29),
        (float('inf'), 33)]

    tax = 0

    currentBracket = 0
    currentStop = 0
    nextStop = 0
    
    while currentStop < income:
        nextStop = min(brackets[currentBracket][0], income)
        addedTaxCents = ((nextStop - currentStop) * brackets[currentBracket][1])
#        print("addedTaxCents ", addedTaxCents)
        tax += (addedTaxCents)
#        print("tax is now ", tax)
        currentBracket+=1
        currentStop = nextStop
    
    tax = round_it(tax) /100

    return tax
