#Kerem Kok
#3/6/21
#A function that takes a year as a parameter and returns True if the year is a leap year, False if it is otherwise.


def leap_Year(year):
    if year % 4 == 0 and year %100 != 0 or year % 400 == 0:    
        return True
    else:
        return False
