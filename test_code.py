class Calculator:
    def __init__(self, name):
        self.name = name

    def add(self, a, b):
        """Returns the sum of two numbers."""
        return a + b

    def multiply(self, a, b):
        """Returns the product of two numbers."""
        return a * b

# Create an instance of Calculator
calc = Calculator("My Calculator")

# Perform addition and multiplication
num1, num2 = 5, 10
sum_result = calc.add(num1, num2)
product_result = calc.multiply(num1, num2)

# Print results
print(f"The sum of {num1} and {num2} is: {sum_result}")
print(f"The product of {num1} and {num2} is: {product_result}")
