# Importing necessary libraries
import asyncio
import random
from typing import List, Tuple, Dict, Any
from functools import wraps
import time
from functools import wraps

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

class University:
    """Outer class representing a university."""

    def __init__(self, name: str):
        self.name = name
        self.departments = []

    def add_department(self, department_name: str):
        department = self.Department(department_name)
        self.departments.append(department)
        return department

    def __str__(self):
        return f"University: {self.name}, Departments: {[dept.name for dept in self.departments]}"

    class Department:
        """Nested class representing a department within a university."""

        def __init__(self, name: str):
            self.name = name
            self.courses = []

        def add_course(self, course_name: str, course_code: str):
            course = self.Course(course_name, course_code)
            self.courses.append(course)
            return course

        def __str__(self):
            return f"Department: {self.name}, Courses: {[course.course_code for course in self.courses]}"

        class Course:
            """Nested class representing a course within a department."""

            def __init__(self, name: str, code: str):
                self.name = name
                self.course_code = code
                self.students = []

            def add_student(self, student_name: str, student_id: int):
                student = self.Student(student_name, student_id)
                self.students.append(student)

            def __str__(self):
                return f"Course: {self.name}, Students: {[student.name for student in self.students]}"

            class Student:
                """Nested class representing a student within a course."""

                def __init__(self, name: str, student_id: int):
                    self.name = name
                    self.student_id = student_id

                def __str__(self):
                    return f"Student: {self.name} (ID: {self.student_id})"


# Example Usage
if __name__ == "__main__":
    # Create a university
    university = University("TechVille University")

    # Add a department
    cs_department = university.add_department("Computer Science")

    # Add courses to the department
    algorithms_course = cs_department.add_course("Algorithms", "CS101")
    ai_course = cs_department.add_course("Artificial Intelligence", "CS102")

    # Add students to the courses
    algorithms_course.add_student("Alice", 1001)
    algorithms_course.add_student("Bob", 1002)
    ai_course.add_student("Charlie", 1003)

    # Print details
    print(university)
    for department in university.departments:
        print(department)
        for course in department.courses:
            print(course)
            for student in course.students:
                print(student)





# def extract_points_of_interest_grouped(self, node: Node, file_extension: str, current_depth: int = 0, max_depth: int = 2) -> List[List[List[Tuple[Node, str]]]]:
#         """
#         Args:
#             node (Node): The current AST node.
#             file_extension (str): The file extension to determine language-specific node types.
#             current_depth (int): The current depth in the node hierarchy.
#             max_depth (int): The maximum depth to process nodes.

#         Returns:
#             List[List[List[Tuple[Node, str]]]]: A list of groups, where each group contains
#                                                 sublists of tuples (Node, Type).
#         """
#         grouping_types = self._get_node_types_of_interest(file_extension)
#         grouped_points = []

#         # Base case: Stop processing if maximum depth is exceeded
#         if current_depth > max_depth:
#             return grouped_points

#         # Process the current node
#         if node.type in grouping_types.keys():
#             # Create a group for the current node
#             current_group = [[(node, grouping_types[node.type])]]
            
#             # Process child nodes and group them recursively
#             for child in node.children:
#                 child_groups = self.extract_points_of_interest_grouped(
#                     child, file_extension, current_depth + 1, max_depth
#                 )
#                 if child_groups:
#                     current_group.extend(child_groups)
            
#             grouped_points.append(current_group)
#         else:
#             # Process children independently if the current node isn't a grouping node
#             for child in node.children:
#                 grouped_points.extend(
#                     self.extract_points_of_interest_grouped(
#                         child, file_extension, current_depth + 1, max_depth
#                     )
#                 )

#         return grouped_points