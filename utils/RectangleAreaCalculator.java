// This is a java file to test the output of the LLM => It is manually filled 
import java.util.Scanner;

public class RectangleAreaCalculator {
    // Function to calculate the area of a rectangle
    public static double calculateArea(double length, double width) {
        return length * width;
    }

    public static void main(String[] args) {
        // Scanner object for reading user input
        Scanner scanner = new Scanner(System.in);

        try {
            // Prompt the user for length and width
            System.out.print("Enter the length of the rectangle: ");
            double length = scanner.nextDouble();

            System.out.print("Enter the width of the rectangle: ");
            double width = scanner.nextDouble();

            // Calculate the area using the calculateArea method
            double area = calculateArea(length, width);

            // Print the result
            System.out.printf("The area of the rectangle is: %.2f%n", area);

        } catch (Exception e) {
            // Handle invalid input
            System.out.println("Invalid input. Please enter numeric values.");
        } finally {
            // Close the scanner to free resources
            scanner.close();
        }
    }
}