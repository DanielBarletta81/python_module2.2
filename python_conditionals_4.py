#Task 1: Leap Year Checker
""" Write a Python program that prompts the user to input a year.
The program should determine if the given year is a leap year or not 
and then display an appropriate message. 
Please note that this is the definition of a leap year: 
Every year that is exactly divisible by four is a leap year,
except for years that are exactly divisible by 100, 
but these centurial years are leap years if they are exactly divisible by 400. """


year_chosen = int(input("Please enter a year: "))

if (year_chosen % 4 == 0) and not (year_chosen % 100 == 0):
    print("The year you entered is a leap year.")
elif(year_chosen % 400 == 0) and (year_chosen % 100 == 0):
    print("The year entered is a leap year.")
else:
    print("The year entered is not a leap year.") 



#Task 2: Century Verification
""" Add functionality to your program from Task 1 to 
inform the user if the entered year is a century year (e.g., 1900, 2000) 
regardless of whether it's a leap year or not. """


if (year_chosen % 100 == 0):
    print("The year entered is a centurial year.")
else:
    print("The year entered is not a centurial year.")


#Task 3: Time Traveler
""" Enhance your program to indicate if the provided year is in the future, past, 
or is the current year,
compared to the a year variable year=2020. """

year = 2020

if (year_chosen == year):
    print("The year entered is the current year.")
elif (year_chosen >= year):
    print("The year entered is in the future!")
else:
    print("The year entered is in the past.")