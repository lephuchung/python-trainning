a = float(input("Enter the first number: "))
operator = input("Enter the operator: ")
b = float(input("Enter the second number: "))

if operator == "+":
    print("Result is " + str(a + b))
elif operator == "-":
    print("Result is " + str(a - b))
elif operator == "*":
    print("Result is " + str(a * b))
elif operator == "/":
    print("Result is " + str(a / b))
else:
    print("Invalid operator!!!")