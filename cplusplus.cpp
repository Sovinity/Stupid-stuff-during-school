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
        std::string x = lowerCase(input(""));
        
        if (x == "exit" || x == "quit")
        {
            return 0;
        }
        else if (findInString(x, "snuggles") || findInString(x, "snuggle") || findInString(x, "cuddles") || findInString(x, "cuddle"))
        {
            std::cout << "C++ isn't nice enough to give snuggles";
        }
        else
        {
            std::cout << "Sorry, I don't understand :/";
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
    return string.find(substring)!=std::string::npos;
}