from Description.generate_description import Description

code_snippet = '''
def calculate_area(length, width):
    return length * width

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = calculate_area(length, width)
print(f"The area of the rectangle is: {area}")
    '''

description = Description(code_snippet)

print("Description of the code:")
#description is an str => need to optimize the output shown
print(description.get_code_description())