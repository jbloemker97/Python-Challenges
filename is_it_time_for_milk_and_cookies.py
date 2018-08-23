'''
Christmas Eve is almost upon us, so naturally we need to prepare some milk and cookies for Santa! Create a function that accepts a Date object and returns True if it's Christmas Eve (December 24th) and False otherwise.
'''

def time_for_milk_and_cookies(date):
  return (date.day==24 and date.month==11)