'''
Given a list of numbers, write a function that returns a list that...
    1.) Has all duplicate elements removed.
    2.) Is sorted from least to greatest value.
'''

def unique_sort(lst):
    duped = []
	
    for x in lst:
        if x not in duped:
            duped.append(x)
		
    return sorted(duped)