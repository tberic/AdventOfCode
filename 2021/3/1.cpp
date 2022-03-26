#include <iostream>
#include <fstream>
#include <string>
#include <bitset>
using namespace std;

int main()
{
    ifstream f("input.txt");
    string s;
    int ones[100] = {0};
    int n = 0, m;
    
    while (getline(f, s))
    {
        n++;
        m = s.size();
        for (int i = 0; i < m; ++i)
            ones[i] += ( s[i] == '1' );
    }

    bitset<5> gamma, epsilon;
    for (int i = 0; i < m; ++i)
        if (ones[m-i-1] >= n/2)
        {
            gamma[i] = 1;
            epsilon[i] = 0;
        }
        else
        {
            gamma[i] = 0;
            epsilon[i] = 1;
        }

    cout << gamma << " " << epsilon << endl;


    cout << gamma.to_ulong() * epsilon.to_ulong() << endl;


    f.close();
    return 0;
}