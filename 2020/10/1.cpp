#include <iostream>
#include <fstream>

#define MAXN 200

using namespace std;

int main()
{
    ifstream f;
    f.open("input.txt");
    int x, n = 0;
    int a[MAXN];

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

    for (int i = 0; i < n; ++i)
        cout << a[i] << " ";
    cout << endl;

    int jolt[4] = {0};
    jolt[a[0]]++;
    for (int i = 0; i < n-1; ++i)
        jolt[a[i+1]-a[i]]++;
    jolt[3]++;

    cout << jolt[1]*jolt[3] << endl;

    f.close();
    return 0;
}