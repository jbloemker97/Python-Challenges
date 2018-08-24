'''
Create a function that takes a string and returns a string in which each character is repeated once.
'''

def double_char(txt):
    return ''.join([char*2 for char in txt])