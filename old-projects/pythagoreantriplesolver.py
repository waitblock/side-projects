from math import *
loop = 'y'
print("Welcome to the Pythagorean Triple Solver!")
print("v0.9.1")
while loop == 'y':
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    num3 = input("Enter third number: ")
    if(num1 == 'unknown'):
        answer = (int(num3))**2-(int(num2))**2
        realAnswer = sqrt((int(num3))**2-(int(num2))**2)
    if(num2 == 'unknown'):
        answer = (int(num3))**2-(int(num1))**2
        realAnswer = sqrt((int(num3))**2-(int(num1))**2)
    if(num3 == 'unknown'):
        answer = (int(num1))**2+(int(num2))**2
        realAnswer = sqrt((int(num1))**2+(int(num2))**2)
    print("sqrt", answer)
    print(realAnswer)
    loop = input("Would you like to solve another triple? ")

#need to debug:
"""if choice == "check":
    while loop == 'y':
        answer = 0
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        num3 = input("Enter third number: ")
        if ((int(num3))**2 - (int(num2))**2) == (int(num1)):
            print("This is a pythagorean triple.")
        elif ((int(num3))**2 - (int(num2))**2) != (int(num1)):
            print("This is not a pythagorean triple.")
        loop = input("Would you like to check another triple? ")"""
