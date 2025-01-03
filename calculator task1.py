#creating a function

def calculator():
    print("welcome to the simple calculator")
    print("choose one operation")
    print("1.Addition")
    print("2.subtraction")
    print("3. Multiplication")
    print("4. division")

    #check the number corresponding to the operation

    operation = input("Enter the number corresponding to the operation:")

    if operation not in ['1','2','3','4']:
        print("invalid give the correct number")
        return
    
    #getting the number for operation 

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))


        if operation == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        elif operation == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        elif operation == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        elif operation == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
            else:
                print(" Division by zero is not allowed.")
    except ValueError:
        print("Invalid input. Please enter numeric values")

#calling the function
calculator()
