'''
Create a function that takes the two lowest numbers in a list, and return the sum of them
'''

def sum_lowest(numbers):
    return sum(sorted(numbers[:2]))