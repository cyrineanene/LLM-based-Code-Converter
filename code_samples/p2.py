# Importing necessary libraries
import asyncio
import random
from typing import List, Tuple, Dict, Any
from functools import wraps
import time

# Metaclass for custom behavior
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# Base class using multiple inheritance
class Animal:
    def speak(self):
        return "Some generic animal sound"

class Mammal:
    def walk(self):
        return "Walking on four legs"

# Dog class with multiple inheritance
class Dog(Animal, Mammal):
    def speak(self):
        return "Woof!"

# Function with advanced decorators
def timing_decorator(func):
    """A decorator to measure the execution time of a function"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    return "Finished"

# Asynchronous function with async/await
async def async_task(id: int) -> str:
    print(f"Task {id} started")
    await asyncio.sleep(random.uniform(0.5, 2.0))
    return f"Task {id} completed"

async def main():
    tasks = [async_task(i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

# Custom exception handling
class NegativeValueError(Exception):
    pass

def process_value(value: int) -> int:
    if value < 0:
        raise NegativeValueError("Value cannot be negative")
    return value ** 2

# Recursive function with dynamic programming
memo = {}
def fibonacci(n: int) -> int:
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

# Class using metaclass and singleton pattern
class Logger(metaclass=SingletonMeta):
    def log(self, message: str) -> None:
        print(f"Log: {message}")

# Function with complex type hints
def process_data(data: List[Dict[str, Any]]) -> Tuple[List[str], int]:
    names = [item['name'] for item in data if 'name' in item]
    total = sum(item.get('value', 0) for item in data)
    return names, total

# Lambda and List Comprehensions
even_squares = [x**2 for x in range(20) if x % 2 == 0]
filtered_squares = list(filter(lambda x: x > 50, even_squares))

# Main block to run all code
if __name__ == "__main__":
    # Singleton Pattern Test
    logger1 = Logger()
    logger2 = Logger()
    print(f"Logger instances are the same: {logger1 is logger2}")

    # Multiple Inheritance Test
    dog = Dog()
    print(dog.speak())  # Should print "Woof!"
    print(dog.walk())   # Should print "Walking on four legs"

    # Decorator Test
    print(slow_function())

    # Async/Await Test
    asyncio.run(main())

    # Exception Handling Test
    try:
        result = process_value(-5)
    except NegativeValueError as e:
        print(f"Error: {e}")

    # Fibonacci Memoization Test
    print(f"Fibonacci of 10: {fibonacci(10)}")

    # Type Hinting and Complex Data Test
    sample_data = [
        {'name': 'Alice', 'value': 10},
        {'name': 'Bob', 'value': 20},
        {'name': 'Charlie', 'value': 30}
    ]
    names, total = process_data(sample_data)
    print(f"Names: {names}, Total value: {total}")

    # Lambda and List Comprehension Test
    print(f"Even squares: {even_squares}")
    print(f"Filtered squares greater than 50: {filtered_squares}")
