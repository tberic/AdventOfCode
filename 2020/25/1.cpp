#include <iostream>
#include <fstream>
#include <string>

#define MOD 20201227

using namespace std;

long long transform(long subject, long a)
{
    long long n = 1;

    while (a)
    {
        a--;
        n *= subject;
        n %= MOD;
    }
    
    return n;
}

int main()
{
    ifstream f;
    long x, y;

    f.open("input.txt");
    f >> x >> y;
    f.close();

    long a = 0, b = 0;
    long n = 1;

    while (n != x)
    {
        a++;
        n *= 7;
        n %= MOD;
    }

    cout << transform(7, a) << endl;
    cout << transform(y, a) << endl;


    return 0;
}