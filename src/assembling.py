class Assembler: 
    def __init__(self, generated_code, file_name):
        self.generated_code = generated_code
        self.file_name = file_name
    def assemble_java_code(self):
        if not self.file_name.endswith(".java"):
            self.file_name += ".java"
        try:
            with open(self.file_name, "a") as file:
                file.write("\n" + self.generated_code)  
                print(f"Java code appended to '{self.file_name}' successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

# java_file_name = "RectangleAreaCalculator"
# java_code_to_add = """
# import java.util.Scanner; 
# public class RectangleAreaCalculator { // Method to calculate the area of a rectangle. 
#     public static double calculateArea(double length, double width) { 
#         // Return the product of length and width. 
#         return length * width; } 
#     public static void main(String[] args) { 
#             // Create a new Scanner object to read user input. 
#             Scanner scanner = new Scanner(System.in); 
#             // Prompt the user to enter the length of the rectangle. 
#             System.out.print("Enter the length of the rectangle: "); 
#             // Read the user input and convert it to a double. 
#             double length = scanner.nextDouble(); 
#             // Prompt the user to enter the width of the rectangle. 
#             System.out.print("Enter the width of the rectangle: "); 
#             // Read the user input and convert it to a double. 
#             double width = scanner.nextDouble(); 
#             // Calculate the area of the rectangle using the calculateArea method. 
#             double area = calculateArea(length, width); 
#             // Print the calculated area. 
#             System.out.println("The area of the rectangle is: " + area); 
#             // Close the Scanner object to prevent resource leaks. 
#             scanner.close(); 
#     } 
# } 
# """
# assemble = Assembler(java_code_to_add, java_file_name)
# assemble.assemble_java_code()