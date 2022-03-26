#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <bitset>

using namespace std;

string mask(36, 'X');

unsigned long long bitmask(unsigned long long x)
{
    bitset<36> b(x);

    for (int i = 0; i < 36; ++i)
        if (mask.at(36-i-1) != 'X')
            b[i] = mask.at(36-i-1)-'0';

    return b.to_ullong();
}

int main()
{
    ifstream f;
    f.open("input.txt");
    string line;
    unsigned long long sum = 0LL;

    unsigned long long mem[100000L] = {0LL};

    while (getline(f, line))
    {
        string lhs = line.substr(0, line.find("=")-1);
        string val = line.substr(line.find("=")+2);

        if (lhs == "mask")
        {
            mask = val;
        }
        else
        {
            istringstream is(val);
            unsigned long long x, location;
            is >> x;

            lhs = lhs.substr(lhs.find("[")+1);
            lhs = lhs.substr(0, lhs.size()-1);

            istringstream is2(lhs);
            is2 >> location;
            
            mem[location] = bitmask(x);
            //cout << "mem[" << location << "] = " << bitmask(x) << "  (" << x << ")" << "   ." << mask << "." <<  endl;
        }
    }

    for (unsigned long long i = 0L; i < 100000L; ++i)
        sum += mem[i];

    cout << sum << endl;


    mask = "10X0110X01100X00111XX00001X011101001";
    cout << bitmask(92667525) << endl;
/*
    bitset<36> b(10);
    cout << b << endl;
    cout << mask << endl;
*/
    f.close();
    return 0;
}