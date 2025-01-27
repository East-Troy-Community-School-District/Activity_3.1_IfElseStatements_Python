'''
Bigger Number
Pawelski
1/27/2025
Instructions:
1.  Predict what the program will do. Check your
    prediction by running the program a few times
    and entering a variety of numbers.
2.  Give an example of two numbers that would
    display multiple messages.
3.  How many if statements can a program contain?
4.  Add a breakpoint on line 20 and step through the
    program in debugging mode. Does the program check
    each if statement? What does this tell you?
'''

number1 = int(input("Enter a number >> "))
number2 = int(input("Enter another number >> "))
if number1 == number2:
    print(str(number1) + " is equal to " + str(number2))
if number1 > number2:
    print(str(number1) + " is bigger than " + str(number2))
if number1 < number2:
    print(str(number2) + " is bigger than " + str(number1))
if number1 >= number2:
    print(str(number1) + " is bigger than or equal to " + str(number2))
if number1 <= number2:
    print(str(number2) + " is bigger than or equal to " + str(number1))
