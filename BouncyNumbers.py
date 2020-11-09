"""Problem: Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""
old_value = {"old_val":0, "min_number":0}

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
    count = old_value["old_val"]
    if isBouncynumber(min_number):
        count += 1
    old_value["old_val"] = count
    return count/min_number
           

"""Main program"""
if __name__ == "__main__":
    percentage = 0.99
   
    #Brute Force Solution
    #This solution find out the least number that its bouncy numbers match with a target percentage 
    n = 100
    while getPercentageBouncyNumber(n) != percentage:
        n += 1
    print(n)
