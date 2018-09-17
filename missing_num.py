'''
Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.
'''

def missing_nums(lst):
    try:
        for num in range(1,11):
            index = lst.index(num)
    except:
        return num