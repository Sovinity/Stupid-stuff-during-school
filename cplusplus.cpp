/*

C Plus PLus file by MushroomEnder!
Put header data in the header file please!

*/

#include "cplusplus.h"

int main() 
{
    std::cout << "Hello World from c++!" << std::endl;
    std::cout << "Welcome to the c++ shell!";
    while (true)
    {
        std::string x = input("");
        
        if (x == "exit" || x == "quit")
        {
            return 0;
        }
        else if (x.find("snuggle")!=std::string::npos)
        {
            std::cout << "C++ isn't nice enough to give snuggles";
        }
    }
}

std::string input(std::string text)
{
    std::string answer;
    std::cout << text << std::endl;
    std::cout << ">>> ";
    std::getline(std::cin, answer);
    return answer;
}

std::string lowerCase(std::string text)
{
    std::transform(text.begin(), text.end(), text.begin(),
    [](unsigned char c){ return std::tolower(c); });
    return text;
}

bool findInString(std::string string, std::string substring)
{
    text
}