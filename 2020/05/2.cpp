#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int convert(string s)
{
    int n = 0;
    int i = 0;

    while (i < s.size())
    {
        n *= 2;
        n += (s.at(i)-'0');
        i++;
    }

    return n;
}

string binarize(string s)
{
    string t(s);
    
    for (int i = 0; i < s.size(); ++i)
    {
        if (s.at(i) == 'F' || s.at(i) == 'L')
            t.at(i) = '0';
        if (s.at(i) == 'B' || s.at(i) == 'R')
            t.at(i) = '1';
    }

    return t;
}

int main()
{
    ifstream f;
    f.open("input.txt");
    string s;
    int x, max = 0, min = 1024;
    int exists[1024] = {0};
    
    while (f >> s)
    {
        x = convert(binarize(s));
        exists[x] = 1;

        if ( x < min )
            min = x;
        if ( x > max )
            max = x;
    }

    for (int i = min; i < max; ++i)
        if (!exists[i])
        {
            cout << i << endl;
            break;
        }

    f.close();
    return 0;
}