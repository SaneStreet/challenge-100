// To use this program:
// You must compile it using the 'csc <your_file_name>.cs' command in Command Prompt
// Then call the .exe file that has been generated
// It's typically called your_file_name.exe

using System;
using System.Linq; // this is needed to use Min() and Max()

class Program
{
    // Main() to run the program
    public static void Main(string[] args){
        // Four integer arrays
        int[] Numbers = {5, 10, 50, 75, 250};
        int[] MoreNumbers = {540, 41, 78, 91, 2};
        int[] OnlyTwoNumbers = {0, 1};
        int[] OnlyOneNumber = {5};
        
        // Calls the method with an argument
        FindMinMax(Numbers);
        FindMinMax(MoreNumbers);
        FindMinMax(OnlyTwoNumbers);
        FindMinMax(OnlyOneNumber);
    }

    // The method used to find the lowest and largest number in an array
    static void FindMinMax(int [] ArrayOfNumbers){
        // assigns an integer variable to the lowest number
        int MinNumber = ArrayOfNumbers.Min();
        // assigns an integer variable to the largest number
        int MaxNumber = ArrayOfNumbers.Max();
        // Writes to the console with the provided list
        Console.WriteLine("From the list provided:");
        // Writes the minimum and maximum numbers to the console
        // using interpolation ($"")
        Console.WriteLine($"Minimum is: {MinNumber}");
        Console.WriteLine($"Maximum is: {MaxNumber}\n");
    }

}
