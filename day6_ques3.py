# Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)
num1 = int(input("Enter 1st number "))
num2 = int(input("Enter 2nd number "))
op = input("Enter the operation you want to perform(+,-,*,/)\n")
if op == "+":
    print("Your required result is", num1+num2)
elif op == "-":
    print("Your required result is", num1-num2)
elif op == "*":
    print("Your required result is", num1*num2)
elif op == "/":
    print("Your required result is", num1/num2)
else:
    print("Wrong choice entered")
