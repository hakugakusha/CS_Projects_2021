num1 = float(input("Please enter a number: "))
operator = input("Enter operator: ")
num2 = float(input("Please enter another number: "))

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    print(num1 / num2)

elif operator == "**":
    print(num1 ** num2)

else:
    print("Invalid Operator")

