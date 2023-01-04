'''
Password
1/4/2023
Python I

Instructions:
Run the program and try entering the password
"password". What happens? Why? Next, try
entering the password "1234". What happens?
Why? How would you modify the program so that
it checks for the password "abcdefg"?
Test your theory by modifying the program.
In your own words, describe how an if/else
statement works.
'''

name = input("Enter your password >> ")
if name == "password":
    print("Access granted!")
else:
    print("Access denied!")