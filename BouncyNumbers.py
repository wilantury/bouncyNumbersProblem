"""Problem: Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""
"""imports"""
import time

count = 0

"""Check if a number is a bouncy number
   Output: Boolean, integer - (isBouncy?, quantity of digits after bouncy digit)
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
            return True, len(iterableNumber) -(i + 2)
    return False, 0

"""Compute the search of the least number that match with the percentage of 
    bouncy numbers.
    arguments: float percentage - target percentage.
    Output: least number that has the quantity of bouncy numbers that match
            with the percentage target. 
"""
def get_least_bouncy_number(percentage):
    global count
    min_number = 101

    while True:
        min_number_iterable = str(min_number)
        is_bouncy, rest = is_bouncy_number(min_number_iterable)
        if is_bouncy:
            if rest > 0:
                power = 10**rest
                bouncy = min_number // power
                while bouncy == min_number // power: 
                    count += 1
                    if count/min_number == percentage:
                        return count, min_number
                    min_number += 1
                min_number -= 1
            else:
                 count += 1
                 if count/min_number == percentage:
                    return count, min_number
        else:
            if count/min_number == percentage:
                return count, min_number   
        min_number += 1      

"""Main program"""
if __name__ == "__main__":
    percentage = 0.99

    #Brute Force Solution, but performance improved, just 360mS in my machine
    #This solution find out the least number that its bouncy numbers match with a target percentage 
    current = time.time()
    print(get_least_bouncy_number(percentage))
    print(time.time() - current)