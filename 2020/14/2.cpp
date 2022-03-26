#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <bitset>
#include <map>

using namespace std;

map<unsigned long long, unsigned long long> mem;

/*
unsigned long long bitmask(unsigned long long x, string mask)
{
    bitset<36> b(x);

    for (int i = 0; i < 36; ++i)
        if (mask.at(36-i-1) == '1')
            b[i] = 1;

    return b.to_ullong();
}
*/

unsigned long long convert(string s)
{
    bitset<36> b;
    for (int i = 0; i < 36; ++i)
        b[i] = s.at(36-i-1) - '0';

    return b.to_ullong();
}

void write(unsigned long long x, string mask)
{
    int t;

    t = 0;
    for (int i = 0; i < mask.size(); ++i)
        if (mask.at(i) == 'X')
        {
            t = 1;
            //cout << mask << endl; 
            mask.at(i) = '0';
            write(x, mask);
            mask.at(i) = '1';
            //cout << mask << endl; 
            write(x, mask);
            return ;
        }

    if (t == 0)
    {
        mem[convert(mask)] = x;
        //cout << "mem[" << convert(mask) << "] = " << x << endl;
    }
}

string maskiraj(unsigned long long location, string mask)
{
    bitset<36> b(location);
    string t(mask);

    for (int i = 0; i < 36; ++i)
        if (mask.at(36-i-1) == '1')
            b[i] = 1;

    for (int i = 0; i < 36; ++i)
        t.at(36-i-1) = ( (mask[36-i-1] == 'X') ? 'X' : (b[i]+'0') );

    return t;
}

int main()
{
    ifstream f;
    f.open("input.txt");
    string line;
    unsigned long long sum = 0LL;
    string mask(36, 'X');

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
            
            write(x, maskiraj(location, mask));
        }
    }

    for (map<unsigned long long, unsigned long long>::iterator it = mem.begin(); it != mem.end(); ++it)
    {
        sum += it->second;
        //cout << "mem[" << it->first << "] = " << it->second << endl;
    }

    cout << sum << endl;

//    write(1, 2, "1X0X");

    f.close();
    return 0;
}