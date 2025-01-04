#include <iostream>
#include <fstream>
#include <string>
#include <array>
using namespace std;

const array<string, 9> number = { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

int isnumber(string s, int pos)
{
    for (int i = 0; i < 9; ++i)
    {
        int j = 0;
        while (pos + j < s.length() && j < number[i].length() && s[pos + j] == number[i][j])
            j++;
        if (j == number[i].length())
            return i + 1;
    }
    return 0;
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout)
    {
        return 1;
    }

    string line;
    int sum = 0;

    while (getline(fin, line))
    {
        if (line == "")
        {
            continue;
        }

        int first = -1, last = -1;
        for (int i = 0; i < line.length(); ++i)
        {
            if (isdigit(line[i]))
            {
                if (first == -1)
                    first = line[i]-'0';
                last = line[i]-'0';
                continue;
            }
            int x = isnumber(line, i);
            if (x)
            {
                if (first == -1)
                    first = x;
                last = x;
            }
        }

        cout << first << last << endl;
        sum += first*10 + last;
    }

    cout << sum << endl;

    fin.close();
    fout.close();
    return 0;
}