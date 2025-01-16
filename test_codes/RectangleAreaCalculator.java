import java.util.Scanner; 
public class RectangleAreaCalculator { // Method to calculate the area of a rectangle. 
    public static double calculateArea(double length, double width) { 
        // Return the product of length and width. 
        return length * width; } 
    public static void main(String[] args) { 
            // Create a new Scanner object to read user input. 
            Scanner scanner = new Scanner(System.in); 
            // Prompt the user to enter the length of the rectangle. 
            System.out.print("Enter the length of the rectangle: "); 
            // Read the user input and convert it to a double. 
            double length = scanner.nextDouble(); 
            // Prompt the user to enter the width of the rectangle. 
            System.out.print("Enter the width of the rectangle: "); 
            // Read the user input and convert it to a double. 
            double width = scanner.nextDouble(); 
            // Calculate the area of the rectangle using the calculateArea method. 
            double area = calculateArea(length, width); 
            // Print the calculated area. 
            System.out.println("The area of the rectangle is: " + area); 
            // Close the Scanner object to prevent resource leaks. 
            scanner.close(); 
    } 
} 