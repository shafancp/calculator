class Calculation:
    def __init__(self):
        pass

    # Function to add two numbers
    def add(self, num1, num2):
        return num1 + num2

    # Function to subtract num2 from num1
    def subtract(self, num1, num2):
        return num1 - num2

    # Function to multiply two numbers
    def multiply(self, num1, num2):
        return num1 * num2

    # Function to divide num1 by num2
    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2


    def square(number):
      return number * number

# Create an instance of the Calculation class
calculator = Calculation()

# Perform arithmetic operations
result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(5, 3)
result_multiply = calculator.multiply(5, 3)
result_divide = calculator.divide(5, 3)

# Display the results
print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)