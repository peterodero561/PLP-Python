"""Bsic calculator program"""

def add(a, b):
    return int(a) + int(b)
def subtract(a, b):
    return int(a) - int(b)
def multiply(a,b):
    return int(a) * int(b)
def divide(a, b):
    return int(a) / int(b)
def menu():
    print("\n\n**Basic math operations using integers**")
    print("1. Addition \n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    operation = int(input("Select any operation: "))
    return operation

while(1):
    operation = menu()
    if operation == 5:
        break
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    if operation == 1:
        print(f"The Addition of {num1} and {num2} is {add(num1, num2)}")
    elif operation == 2:
        print(f"The Subtraction of {num2} from {num1} is {subtract(num1, num2)}")
    elif operation == 3:
        print(f"The multiplication of {num1} by {num2} is {multiply(num1, num2)}")
    elif operation == 4:
        print(f"The division of {num1} by {num2} is {divide(num1, num2)}")
    else:
        print("Please choose an number option from the given menu")
