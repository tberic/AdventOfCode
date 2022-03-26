#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int a[1100];
int n = 0;

int main()
{
    ifstream f;
    f.open("input.txt");
    long target = 1398413738, sum = 0;
    int i, j;

    while (f >> a[n++]);

    for (i = 0; i < n; ++i)
    {
        sum = 0;
        j = i;
        while (sum < target && j < n)
            sum += a[j++];
        if (sum == target)
        {
            cout << i+1 << " " << j << endl;
            cout << a[i]+a[j-1] << endl;
            break;
        }
    }

    f.close();
    return 0;
}