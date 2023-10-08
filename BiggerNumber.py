'''
Bigger Number
Pawelski
10/8/2023
Introduction to Computer Science

Instructions:
Run the program and try entering a variety
of numbers. What happens? Why? Give an example
of two numbers that would display multiple
messages. In your own words, describe how
seperate if statements works.
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