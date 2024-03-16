
#Task 1: Identify the Greatest

""" Write a Python program that prompts the user to enter three numbers. 
The program should then identify and 
print out the largest number among the three. """

user_number1 = input('Enter your first lucky number: ')
user_number2 = input('Enter your next lucky number: ')
user_number3 = input('Enter your last lucky number: ')

if (user_number1 >= user_number2) and (user_number1 >= user_number3):
    print("Largest number = " + user_number1)
elif (user_number2 >= user_number1) and (user_number2 >= user_number3):
    print("Largest number = " + user_number2)
else:
    print("Largest number = " + user_number3)



#Task 2: Identify the Smallest

""" Extend your program from Task 1 to also determine the 
smallest number among the three and print it out. """

if (user_number1 <= user_number2) and (user_number1 <= user_number3):
    print("Smallest number = " + user_number1)
elif (user_number2 <= user_number1) and (user_number2 <= user_number3):
    print("Smallest number = " + user_number2)
else:
    print("Smallest number = " + user_number3)




#Task 3: Equality Check

""" Enhance your program to handle cases where
two or all of the numbers are equal.
The program should display appropriate messages like 
"Two numbers are equal and the largest" or "All numbers are equal". """

if (user_number1 == user_number2 == user_number3):
    print("All numbers are equal: " + user_number1)
elif (user_number2 == user_number1) or (user_number2 == user_number3) or user_number1 == user_number3:
    print("Two numbers are the largest")
else:
    print("All 3 numbers are unique.")