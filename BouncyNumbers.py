"""Problem: Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""
"""imports"""
import time

old_value = 0

"""Check if a number is a bouncy number
   Output: Boolean
"""
def is_bouncy_number(iterableNumber):
    increasing = True
    decreasing = True
    for i in range(0 ,len(iterableNumber)-1):
        num_1 = iterableNumber[i+1]
        num_2 = iterableNumber[i]
        if num_1 >= num_2:
            increasing = increasing
        else:
            increasing = False
        if num_2 >= num_1:
            decreasing = decreasing
        else:
            decreasing = False
        if increasing == decreasing == False:
            return True
    return False

"""Compute the percentage of bounce numbers in a range.
    arguments: min_number - integer that fix a range.
    Output: float - percentage
"""
def get_percentage_bouncy_number(min_number):
    global old_value
    count = old_value
    if is_bouncy_number(str(min_number)):
        count += 1
    old_value = count
    return count/min_number
           

"""Main program"""
if __name__ == "__main__":
    percentage = 0.99

    #Brute Force Solution
    #This solution find out the least number that its bouncy numbers match with a target percentage 
    n = 101
    current = time.time()
    while get_percentage_bouncy_number(n) != percentage:
        n += 1    
    print(n)
    print(time.time() - current)