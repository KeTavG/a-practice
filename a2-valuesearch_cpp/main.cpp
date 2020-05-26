#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

int getInt()
{
    int value = 0;
    char checking = '\0';
    bool flag = false;
    while (!flag)
    {
        std::cin >> value;
        checking = std::cin.get();
        if (std::cin.fail() || (checking != '\n'))
        {
            std::cout << "You entered an invaild value. Try again!" << std::endl;
            std::cout << "value = ";
            std::cin.clear();
            while (std::cin.get() != '\n')
                ;
        }
        else
        {
            flag = true;
        }
    }
    return value;
}

int getLength()
{
    int length = 0;
    bool flag = false;
    while (!flag)
    {
        length = getInt();
        if (length <= 0)
        {
            std::cout << "Length should be longer than zero. Try again!" << std::endl;
            std::cout << "Array length = ";
        }
        else
        {
            flag = true;
        }
    }
    return length;
}

std::vector<int> createArray()
{
    std::cout << "Enter the array. " << std::endl;
    std::cout << "Array length = ";
    int length = getLength();
    std::vector<int> arr(length);
    for (int i = 0; i < length; ++i)
    {
        std::cout << "arr[" << i << "] = ";
        arr[i] = getInt(); 
    }
    return arr;
}

int getMin(std::vector<int> arr)
{
    int minVal = arr[0];
    if (arr.size() > 1)
    {
        std::for_each(++(arr.begin()), arr.end(), [&minVal](const int &num) { minVal = (num < minVal) ? num : minVal; });
    }
    return minVal;
}

int getMax(std::vector<int> arr)
{
    int maxVal = arr[0];
    if (arr.size() > 1)
    {
        std::for_each(++(arr.begin()), arr.end(), [&maxVal](const int &num) { maxVal = (num > maxVal) ? num : maxVal; });
    }
    return maxVal;
}

int getMode(std::vector<int> arr)
{
    int mode = arr[0];
    if (arr.size() > 2)
    {
        std::vector<int> elemArr;
        std::vector<int> countArr;
        for (const int &num : arr)
        {
            bool findFlag = false;
            for (int i = 0; i < elemArr.size(); ++i)
            {
                if (elemArr[i] == num)
                {
                    findFlag = true;
                    ++countArr[i];
                    break;
                }
            }
            if (!findFlag)
            {
                elemArr.push_back(num);
                countArr.push_back(1);
            }
        }
        int maxId = 0;
        int maxCount = countArr[0];
        for (int i = 1; i < countArr.size() ; ++i)
        {
            if (countArr[i] > maxCount)
            {
                maxId = i;
                maxCount = countArr[i];
            }
        }
        mode = elemArr[maxId];
    }
    return mode;
}

double getAverage(std::vector<int> arr)
{
    double sum = 0;
    for (const int &num : arr)
        sum += num;
    return (sum / arr.size());
}

int main()
{
    std::vector<int> arr = createArray();
    std::cout << "Your array: { ";
    std::for_each(arr.begin(), arr.end(), [](const int &num) { std::cout << num << ' '; });
    std::cout << '}' << std::endl;
    std::cout << "Minimum value = " << getMin(arr) << std::endl;
    std::cout << "Maximum value = " << getMax(arr) << std::endl;
    std::cout << "Mode = " << getMode(arr) << std::endl;
    std::cout << "Average value = " << getAverage(arr) << std::endl;
    std::cin.get();
    return 0;
}