class SimpleCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

calculator = SimpleCalculator()

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
else:
    result = None
    if choice == '1':
        result = calculator.add(num1, num2)
    elif choice == '2':
        result = calculator.subtract(num1, num2)
    elif choice == '3':
        result = calculator.multiply(num1, num2)
    elif choice == '4':
        result = calculator.divide(num1, num2)
    else:
        print("Invalid choice")
        
    if result is not None and result != "Error: Division by zero":
        print("Result:", result)
    elif result == "Error: Division by zero":
        print(result)
