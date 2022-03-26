#include <iostream>
#include <map>

using namespace std;

int main()
{
    long x, y, n;
    map<long, long> last;

    last[2] = 0;
    last[0] = 1;
    last[6] = 2;
    last[12] = 3;
    last[1] = 4;
    n = 5;
    x = 3;

    //while (n < 30000000)
    while (n < 30000000-1)
    {
        if (last.count(x) == 0)
        {
            last[x] = n;
            x = 0;
            n++;
        }
        else
        {
            y = n-last[x];
            last[x] = n;
            x = y;
            n++;
        }

        //cout << x << " ";
    }

/*
    for (int i = 0; i < 2020; ++i)
        cout << a[i] << " ";
    cout << endl;
*/
    //cout << a[30000000-1] << endl;

    cout << endl << x << endl;

    return 0;
}