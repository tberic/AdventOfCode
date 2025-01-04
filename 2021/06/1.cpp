#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    ifstream f("input.txt");
    int x;
    char c;
    long long timer[9] = {0};
    
    while (f >> x >> c)
        timer[x]++;
    f >> x;
    timer[x]++;

    for (int day = 1; day <= 80; ++day)
    {
        // deal with zero times
        int zeros = timer[0];
        
        for (int i = 1; i <= 8; ++i)
            timer[i-1] = timer[i];
        
        timer[6] += zeros;
        timer[8] = zeros;
    }

    long long count = 0;
    for (int i = 0; i <= 8; ++i)
        count += timer[i];
    cout << count << endl;

    f.close();
    return 0;
}