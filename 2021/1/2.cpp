#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream f("input.txt");
    int a, b, c, x;
    int count = 0;

    f >> a >> b >> c;
    
    while (f >> x)
    {
        if (b+c+x > a+b+c)
            count++;

        a = b;
        b = c;
        c = x;
    }

    cout << count << endl;

    f.close();
    return 0;
}