#include "./start.h"

// "(python3.10 --version || install-pkg python3.10) && npm install prompt-sync && clear && python3.10 main.py"

int main() 
{
    print("BIOS Starting...");
}

std::string print(std::string text)
{
    std::cout << text << std::endl;
    return text;
}

std::string input(std::string text)
{
    if (text != "")
    {
        text += "\n";
    }
    text += ">>> ";
    std::string answer;
    std::getline(std::cin, answer);

    return answer;
}