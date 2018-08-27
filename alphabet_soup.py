'''
Create a function that takes a string and returns a string with its letters in alphabetical order.
'''

def alphabet_soup(txt):
    return "".join(sorted(list(txt.lower())))

