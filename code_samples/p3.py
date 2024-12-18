class Calculator:
    def __init__(self, value=0):
        self.value = value  # declaration of an instance variable

    def add(self, amount):
        self.value += amount
        return self.value

    def subtract(self, amount):
        self.value -= amount
        return self.value


# Example usage
calc = Calculator(10)
print(calc.add(5))  # Output: 15
print(calc.subtract(3))  # Output: 12
