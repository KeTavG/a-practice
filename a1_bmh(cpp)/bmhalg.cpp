#include "bmhalg.h"
#include <vector>
#include <string>

std::vector<size_t> createOffsetTable(std::string img)
{
    size_t imgLength = img.length();
    std::vector<size_t> d(imgLength);
    if (imgLength > 1)
    {
        d[imgLength - 2] = 1;
        size_t count = 2;
        for (size_t i = imgLength - 2; i > 0; --i)
        {
            for (size_t j = 1; j < count; ++j)
            {
                if (img[i - 1] == img[imgLength - 1 - j])
                {
                    d[i - 1] = d[imgLength - 1 - j];
                    break;
                }
                d[i - 1] = count;
            }
            ++count;
        }
        for (size_t i = imgLength - 1; i > 0; --i)
        {
            if (img[i - 1] == img[imgLength - 1])
            {
                d[imgLength - 1] = d[i - 1];
                break;
            }
            d[imgLength - 1] = imgLength;
        }
    }
    else
    {
        d[imgLength - 1] = imgLength;
    }
    return d;
}

size_t algBMH(std::string str, std::string img)
{
    std::vector<size_t> d = createOffsetTable(img);
    size_t strLength = str.length();
    size_t imgLength = img.length();
    size_t index = strLength;
    bool findFlag = false;
    size_t count = imgLength;
    while (count <= strLength)
    {
        size_t tmpCount = count;
        for (size_t i = imgLength; i > 0; --i)
        {
            if (img[i - 1] != str[tmpCount - 1])
            {
                if (tmpCount == count)
                {
                    size_t offset = imgLength;
                    for (size_t j = imgLength - 1; j > 0; --j)
                    {
                        if (str[tmpCount - 1] == img[j - 1])
                        {
                            offset = d[j - 1];
                            break;
                        }
                    }
                    count += offset;
                }
                else
                {
                    count += d[imgLength - 1];
                }
                findFlag = false;
                break;
            }
            findFlag = true;
            --tmpCount;
        }
        if (findFlag)
        {
            index = count - imgLength;
            break;
        }
    }
    return index;
}