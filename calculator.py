# Building a simple calculator

operators = ['+', '-', '*', '/', '%', '**']
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == '+':
    total = num1 + num2
    print('Your Sum Total is : ', total )

elif operator == '-':
    total = num1 - num2
    print('Your Subtraction Total is : ', total )

elif operator == '*':
    total = num1 * num2
    print('Your Multiplication Total is : ', total )

elif operator == '/':
    total = num1 / num2
    print('Your Division Total is : ', total )

elif operator == '%':
    total = num1 % num2
    print('Your Modulus Total is : ', total )

elif operator == '**':
    total = num1 ** num2
    print('Your Exponent Total is : ', total )

else:
    print("Invalid operator. Please choose from +, -, *, /, %, **.")