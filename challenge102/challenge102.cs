// To use this program:
// You must compile it using the 'csc <your_file_name>.cs' command in Command Prompt
// Then call the .exe file that has been generated
// It's typically called your_file_name.exe

using System;
using System.Linq;

class Program
{
    public static void Main(string[] args){
        NameShuffle("Michael Hansen");
        NameShuffle("Donald Trump");
        NameShuffle("Varian Wrynn");
        NameShuffle("Darth Vader");    
    }

    static void NameShuffle(string Name){
        string First = Name.Split()[0];
        string Last = Name.Split()[1];

        Console.WriteLine(Last + " " + First);
    }
}