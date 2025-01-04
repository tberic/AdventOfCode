#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream f;    
    int x, n = 0;
    int a[500];

    f.open("input.txt");
    while (f >> x)
        a[n++] = x;
    f.close();

    for (int i = 0; i < n; ++i)
        for (int j = i+1; j < n; ++j)
            for (int k = j+1; k < n; ++k)
                if (a[i]+a[j]+a[k] == 2020)
                    cout << a[i]*a[j]*a[k] << endl;
    
    return 0;
}