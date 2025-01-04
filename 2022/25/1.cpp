#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
using namespace std;

long long convertToDecimal(string s)
{
    long long result = 0;
    long long power = 1;
    for (int i = s.size()-1; i >= 0; --i)
    {
        if (s[i] >= '0' && s[i] <= '2')
            result += (s[i]-'0') * power;
        else if (s[i] == '-')
            result -= power;
        else if (s[i] == '=')
            result -= 2 * power;

        power *= 5;
    }

    return result;
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout) { return 1; }

    string line;
    long long sum = 0;
    while (getline(fin, line))
    {
        int x = convertToDecimal(line);
        cout << x << endl;
        sum += x;
    }

    cout << sum << endl;

    fin.close();
    fout.close();
    return 0;
}