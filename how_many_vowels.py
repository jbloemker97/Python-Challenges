'''
Create a function that takes a string and returns the number (count) of vowels contained within it.
'''

def count_vowels(txt):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return len([i for i in list(txt) if i in vowels])

