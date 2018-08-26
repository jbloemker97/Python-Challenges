'''
Create a function that takes a string (will be a persons first and last name) and returns a string with the first and last name swapped
'''

def name_shuffle(txt):
    first, last = txt.split(" ")
    return " ".join([last, first])

