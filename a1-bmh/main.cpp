#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include <conio.h>
#include "bmhalg.h"

bool validCheck(std::string str)
{
    bool strValidFlag = false;
    size_t strLength = str.length();
    for (size_t i = 0; i < strLength; ++i)
    {
        if ((str[i] < 0) || (str[i] > 127))
        {
            strValidFlag = false;
            break;
        }
        strValidFlag = true;
    }
    if (!strValidFlag)
        std::cout << "Invalid value!" << std::endl;
    return strValidFlag;
}

int main()
{
    std::string str;
    bool strValidFlag = false;
    while (!strValidFlag)
    {
        std::cout << "Enter a line (Latin only): ";
        std::getline(std::cin, str);
        if (!str.empty())
        {
            strValidFlag = validCheck(str);
        }
        else
        {
            std::cout << "Empty string!" << std::endl;
        }
    }
    std::string img;
    bool imgValidFlag = false;
    while (!imgValidFlag)
    {
        std::cout << "Enter a line image (Latin only): ";
        std::getline(std::cin, img);
        if (!img.empty())
        {
            if (img.length() < str.length())
            {
                imgValidFlag = validCheck(img);
            }
            else
            {
                std::cout << "The line image should be smaller than the line!" << std::endl;
            }
            
        }
        else
        {
            std::cout << "Empty string!" << std::endl;
        }
    }
    std::cout << "Line: " << str << std::endl;
    std::cout << "Line image: " << img << std::endl;
    std::cout << "Select the register sensitivity option:" << std::endl;
    std::cout << "1. Sensitive" << std::endl;
    std::cout << "2. Insensitive" << std::endl;
    bool sensFlag = false;
    while (!sensFlag)
    {
        switch (_getch())
        {
        case '1':
            sensFlag = true;
            break;
        case '2':
            std::for_each(str.begin(), str.end(), [](char& ch) { ch = std::tolower(ch); });
            std::for_each(img.begin(), img.end(), [](char &ch) { ch = std::tolower(ch); });
            sensFlag = true;
            break;
        }
    }
    size_t index = algBMH(str, img);
    if (index != str.length())
    {
        std::cout << "The index of the first entry img into str: " << index << std::endl;
    }
    else
    {
        std::cout << "No entry found." << std::endl;
    }
    return 0;
}
