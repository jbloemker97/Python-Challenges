'''
Create a function that takes a string, checks if it has the same number of 'x's and 'o's and returns either True or False.
'''

def XO(txt):
    	x = 0
	o = 0
	
	for letter in list(txt):
		if letter.lower() == 'x':
			x+=1
		elif letter.lower() == 'o':
			o+=1

	if x == o:
		return True

	return False
