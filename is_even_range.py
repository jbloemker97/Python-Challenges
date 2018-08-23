'''
Using list comprehensions, create a function that finds all even numbers from 1 to the given number.
'''

def find_even_nums(num):
    return [even for even in range(1, num + 1) if even % 2 == 0]