#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <bitset>
using namespace std;

int main()
{
    ifstream f("input.txt");
    string s;
    vector<string> num, original;
    vector<string> keep;
    int m;
    
    while (getline(f, s))
        num.push_back(s);
    m = num[0].size();
    original = num;

    int ones;
    char c;
    for (int pos = 0; pos < m && num.size() > 1; ++pos)
    {
        ones = 0;
        for (int i = 0; i < num.size(); ++i)
            ones += (num[i][pos] == '1');

        if (2*ones >= num.size())
            c = '1';
        else
            c = '0';

        for (int i = 0; i < num.size(); ++i)
            if (num[i][pos] == c)
            {
                keep.push_back(num[i]);
            }

        num = keep;
        keep.clear();
    }

    string O2 = num[0];


    num = original;

    for (int pos = 0; pos < m && num.size() > 1; ++pos)
    {
        ones = 0;
        for (int i = 0; i < num.size(); ++i)
            ones += (num[i][pos] == '1');

        if (2*ones < num.size())
            c = '1';
        else
            c = '0';

        for (int i = 0; i < num.size(); ++i)
            if (num[i][pos] == c)
            {
                keep.push_back(num[i]);
            }

        num = keep;
        keep.clear();
    }

    string CO2 = num[0];

    cout << O2 << " " << CO2 << endl;

    bitset<32> b1(O2), b2(CO2);
    cout << b1.to_ulong() * b2.to_ulong() << endl;


    f.close();
    return 0;
}