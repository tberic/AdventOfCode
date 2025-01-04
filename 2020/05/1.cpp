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
    string s, maks("0000000000");
    int max = 0;
    
    while (f >> s)
    {
        if ( binarize(s) > maks )
            maks = binarize(s);
    }

    cout << maks << endl;

    cout << convert(maks) << endl;

    f.close();
    return 0;
}