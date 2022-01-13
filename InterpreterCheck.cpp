#include <iostream>

using namespace std;

string print(string text);

int main() 
{
    print("Checking for interpreter...\n(It better be 3.10 or higher xD)");

    if (system("python --version") == 0)
    {
        print("Done. (I don't know if it is 3.10, but it better be)");
    }
    else 
    {
        print("A python interpreter could not be found. Exiting...");
        return 1234;
    }
}

string print(string text)
{
    cout << text << endl;
    return text;
}