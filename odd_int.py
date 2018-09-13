'''
Create a function that takes a list and finds the integer which appears an odd number of times.
'''

def find_odd(lst):
    for num in lst:
        if lst.count(num) % 2 != 0:
            return num

