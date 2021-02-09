// To run this script in Command Prompt: 
// write 'node your_file_name.js'
// example: 'node challenge101.js'

// Four different arrays
const numbers = [5, 10, 50, 75, 250];
const moreNumbers = [540, 41, 78, 91, 2];
const onlyTwoNumbers = [0, 1];
const onlyOneNumber = [5];

// A function with a parameter, requiring an array
function FindMinMax (arrayOfNumbers){
    // Finds the min number with the built-in Math.min() function
    const minimumNumber = Math.min(...arrayOfNumbers);
    // Finds the max number with the built-in Math.max() function
    const maximumNumber = Math.max(...arrayOfNumbers);

    // Log a message with the values from the list
    // Logs both minimum and maximum number
    console.log("Find the minimum and maximum of this list.");
    console.log("Minimum is " + minimumNumber);
    console.log("Maximum is " + maximumNumber + '\n');
}

// Function calls
FindMinMax(numbers);
FindMinMax(moreNumbers);
FindMinMax(onlyTwoNumbers);
FindMinMax(onlyOneNumber);