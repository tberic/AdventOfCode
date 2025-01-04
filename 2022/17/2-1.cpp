#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
using namespace std;

int main()
{
    int a = 142;
    int lineA = 206;
    int T = 1877 - 142;
    int linesT = 2879 - 206;

    long long N = 1000000000000;

    long long n = floor( double(N - a) / T);
    cout << n << endl;

    cout << N - n * T - a << endl;

    cout << lineA + n * linesT + 2876 << endl;

    return 0;
}