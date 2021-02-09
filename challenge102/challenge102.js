/*
To use the script in Command Prompt:
write 'node your_file_name.js'
*/

// Function that takes a string
function NameShuffle(name){
    // splits the string, and assigns the array to 'fullname'
    var fullname = name.split(' ');
    // logs 'fullname' with the values of indexes [0] and [1]
    console.log(fullname[1] + ' ' + fullname[0]);
}

// Function calls with arrguments
NameShuffle("Michael Hansen");
NameShuffle("Barack Obama");
NameShuffle("Frodo Baggins");
NameShuffle("Anakin Skywalker");