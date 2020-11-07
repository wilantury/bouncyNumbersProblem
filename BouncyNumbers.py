""""""
from typing import Counter


def isIncreasing(iterableNumber):
    increasing = False
    if len(iterableNumber) == 1:
        return True
    for i in range(0 ,len(iterableNumber)-1):
        if iterableNumber[i+1] > iterableNumber[i] or iterableNumber[i+1] == iterableNumber[i]:
            increasing = True
        else:
            increasing = False
            break
    return increasing

""""""
def isDecreasing(iterableNumber):
    decreasing = False
    if len(iterableNumber) == 1:
        return True
    for i in range(0 ,len(iterableNumber)-1):
        if iterableNumber[i] > iterableNumber[i+1] or iterableNumber[i] == iterableNumber[i+1]:
            decreasing = True
        else:
            decreasing = False
            break
    return decreasing

def isBouncynumber(number):
    iterableNumber = [int(i) for i in str(number)]
    if isDecreasing(iterableNumber) == isIncreasing(iterableNumber) == False:
        return True
    return False


def getPercentageBouncyNumber(min_number):
    count = 0
    for i in range(100,min_number+1):
        if isBouncynumber(i):
            count += 1            
    print(count/min_number)
    print(count)
    print(min_number)
    #return round(count/min_number,2)
    return count/min_number


def getMinNumber(percentage):
    min_number=200
    lower_limit = 0
    old_upper = 0
    upper_limit = min_number

    while(True):
        per = getPercentageBouncyNumber(min_number)
        if per > percentage:
            break
        elif per < percentage:
            lower_limit = min_number
            min_number *= 2
            upper_limit = min_number
    
    while(True):
        per = getPercentageBouncyNumber(min_number)
        if per > percentage:
            old_upper = upper_limit
            min_number = upper_limit -lower_limit
            min_number = lower_limit + min_number // 2
            upper_limit = min_number
            print(min_number)
        elif per < percentage:
            lower_limit = min_number
            min_number = old_upper - lower_limit
            min_number = lower_limit + min_number // 2
            upper_limit = min_number  
            print(min_number)
        elif per == percentage:
            print(per)
            return True      
           


if __name__ == "__main__":
    #getMinNumber(0.50)
    getPercentageBouncyNumber(536)
