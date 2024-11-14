import math
from functools import lru_cache
import random

PI_CONSTANT = 3.14159
MAX_ITER = 10

def debug(func):
    """A decorator that prints function calls"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

class Circle:
    instances_created = 0
    
    def __init__(self, radius):
        self.radius = radius
        Circle.instances_created += 1
    
    @classmethod
    def total_instances(cls):
        return cls.instances_created
    
    @staticmethod
    def area(radius):
        return PI_CONSTANT * (radius ** 2)
    
    @debug
    def perimeter(self):
        return 2 * PI_CONSTANT * self.radius

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        result = None
    finally:
        return result

def power(n):
    def nth_power(x):
        return x ** n
    return nth_power

# Recursive function with memoization
@lru_cache(maxsize=None)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Lambda functions, list comprehensions, and map/filter
square = lambda x: x * x
squares = [square(x) for x in range(10) if x % 2 == 0]
random_doubles = list(map(lambda x: x * 2, filter(lambda x: x > 5, random.sample(range(10), 5))))

# Context manager
class FileOpener:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)
    
    def __enter__(self):
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Main block demonstrating different function calls and data handling
if __name__ == "__main__":
    # Class usage
    circle = Circle(5)
    print(f"Area: {Circle.area(circle.radius)}")
    print(f"Perimeter: {circle.perimeter()}")
    print(f"Total instances: {Circle.total_instances()}")

    # Generator usage
    print("Fibonacci sequence:", list(fibonacci(10)))

    # Exception handling test
    print("Division test:", divide(10, 0))

    # Nested function and closure
    square_function = power(2)
    print("Square of 4:", square_function(4))

    # Recursion with memoization
    print("Factorial of 5:", factorial(5))

    # Lambda functions, comprehensions, map/filter
    print("Squares of even numbers:", squares)
    print("Filtered and doubled values:", random_doubles)

    # Context manager
    with FileOpener("sample.txt", "w") as f:
        f.write("Testing context manager.\n")
