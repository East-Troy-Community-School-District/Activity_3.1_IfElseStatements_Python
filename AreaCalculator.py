'''
Area Calculator
Pawelski
1/27/2025

Instructions:
1.  Predict what the program will do. Check your prediction
    by running the program.
2.  What do the if statements (lines  and ) do in this program?
3.  What happens if you enter "RECTANGLE" for the first question? Why?
4.  Modify the program by allowing the user to enter "triangle"
    so that they can calculate the area of a triangle
    (HINT: the area of a triangle is 0.5 * length * height).
'''

shape = input("Enter a shape >> ")
if shape == "rectangle":
    length = int(input("Length >> "))
    width = int(input("Width >> "))
    area = length * width
    print("Area =", area)
if shape == "circle":
    radius = int(input("Radius >> "))
    area = 3.14 * radius**2
    print("Area =", area)
# Add your code here!