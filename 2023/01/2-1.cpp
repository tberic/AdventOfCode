#include <iostream>
#include <fstream>
#include <string>
#include <map>

const std::map<std::string, int> numbers = {
        {"1", 1}, 
        {"2", 2}, 
        {"3", 3}, 
        {"4", 4}, 
        {"5", 5}, 
        {"6", 6}, 
        {"7", 7}, 
        {"8", 8}, 
        {"9", 9},
        {"one", 1}, 
        {"two", 2}, 
        {"three", 3}, 
        {"four", 4}, 
        {"five", 5}, 
        {"six", 6}, 
        {"seven", 7}, 
        {"eight", 8}, 
        {"nine", 9}
    };

int main()
{
    std::ifstream fin("input.txt");
    std::ofstream fout("output.txt");

    if (!fin || !fout)
        return 1;

    std::string line;
    int sum = 0;
    int pos, posFirst, posLast, first, last;

    while (getline(fin, line))
    {
        if (line == "")
            continue;

        posFirst = line.length();
        posLast = -1;

        for (const auto el : numbers)
        {
            pos = line.find(el.first);
            if (pos != std::string::npos && pos < posFirst)
            {
                posFirst = pos;
                first = el.second;
            }
            pos = line.rfind(el.first);
            if (pos != std::string::npos && pos > posLast)
            {
                posLast = pos;
                last = el.second;
            }
        }

        // std::cout << first << " " << last << std::endl;
        sum += first*10 + last;
    }

    std::cout << sum << std::endl;

    fin.close();
    fout.close();
    return 0;
}