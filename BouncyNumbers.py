"""Problem: Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

"""Check if the number is an increasing number
    Argument: iterableNumber - List with digits
    Output: Boolean
"""
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

"""Check if the number is an decreasing number
    Argument: iterableNumber - List with digits
    Output: Boolean
"""
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

"""Check if a number is a bouncy number
    Argument: number - integer
    output: Boolean
"""
def isBouncynumber(number):
    iterableNumber = [int(i) for i in str(number)]
    if isDecreasing(iterableNumber) == isIncreasing(iterableNumber) == False:
        return True
    return False

"""Compute the percentage of bounce numbers in a range.
    arguments: min_number - integer that fix a range.
    Output: float - percentage
"""
def getPercentageBouncyNumber(min_number):
    count = 0
    for i in range(100,min_number+1):
        if isBouncynumber(i):
            count += 1            
    return count/min_number

"""Algorithm that find a number that its bouncy numbers match with a target percentage
    Input: float - a percentage target
    Output: integer - number that its bouncy numbers match with a target percentage
"""
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
        elif per < percentage:
            lower_limit = min_number
            min_number = old_upper - lower_limit
            min_number = lower_limit + min_number // 2
            upper_limit = min_number  
        elif per == percentage:
            return min_number      
           

"""Main program"""
if __name__ == "__main__":
    #This solution find out a number that match with the target percentage.
    #But Not te first number 
    getMinNumber(0.50)
    
    #Brute Force Solution
    #This solution find out a number that its bouncy numbers match with a target percentage 
    #But it has poor performance
    n = 100
    percentage = 0.5
    while getPercentageBouncyNumber(n) != percentage:
        n += 1
    print(n)
