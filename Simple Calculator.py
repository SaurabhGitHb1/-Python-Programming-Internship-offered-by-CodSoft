num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

operation = input("Enter operation: ")

if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", result)
elif operation == "/":
    result = num1 / num2
    print("Result:", result)
else:
    print("Invalid operation")





Output
Enter first number: 58
Enter second number: 44
Choose operation:
+ for Addition
- for Subtraction
* for Multiplication
/ for Division
Enter operation: *
Result: 2552.0
