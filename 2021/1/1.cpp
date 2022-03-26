#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream f("input.txt");
    int x, last = -1;
    int count = 0;

    f >> last;
    
    while (f >> x)
    {
        if (x > last)
            count++;

        last = x;
    }

    cout << count << endl;

    f.close();
    return 0;
}