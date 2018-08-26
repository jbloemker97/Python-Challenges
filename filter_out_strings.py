'''
Create a function that takes a list of non-negative numbers / strings and returns a new list without the strings.
'''

def filter_list(lst):
    return [num for num in lst if isinstance(num, str) == False]

