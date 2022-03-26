#include <iostream>
#include <fstream>

#define MAXN 200

using namespace std;

int a[MAXN], n = 0;
long long ways[MAXN];

long long count(int pos)
{
    if (pos == 0)
        return 1;
    if (ways[pos] != -1)
        return ways[pos];
    
    long long sum = 0;
    int x = a[pos--];
    while (pos >= 0 && x - a[pos] <= 3)
    {
        ways[pos] = count(pos);
        sum += ways[pos];
        pos--;
    }
    return sum;
}

int main()
{
    ifstream f;
    f.open("input.txt");
    int x;

    a[n++] = 0;
    while (f >> x)
        a[n++] = x;

    for (int i = 0; i < n; ++i)
        for (int j = i+1; j < n; ++j)
            if (a[i] > a[j])
            {
                int t = a[i];
                a[i] = a[j];
                a[j] = t;
            }
    a[n] = a[n-1] + 3;

    for (int i = 0; i <= n; ++i)
        ways[i] = -1;

    cout << count(n) << endl;

    f.close();
    return 0;
}