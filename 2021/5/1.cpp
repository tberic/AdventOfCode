#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

int grid[1001][1001];

int main()
{
    ifstream f("input.txt");
    string line;    

    for (int i = 0; i <= 1000; ++i)
        for (int j = 0; j <= 1000; ++j)
            grid[i][j] = 0;

    while (getline(f, line))
    {
        stringstream s(line);
        int x1, y1, x2, y2;
        char c;
        s >> x1 >> c >> y1 >> c >> c >> x2 >> c >> y2;

        cout << x1 << " " << y1 << " " << x2 << " " << y2 << endl;

        if (x1 > x2)
            swap(x1, x2);
        if (y1 > y2)
            swap(y1, y2);

        if (x1 == x2)
            for (int i = y1; i <= y2; ++i)
                grid[x1][i]++;
        if (y1 == y2)
            for (int i = x1; i <= x2; ++i)
                grid[i][y1]++;
    }

    int count = 0;
    for (int i = 0; i <= 1000; ++i)
        for (int j = 0; j <= 1000; ++j)
            if (grid[i][j] > 1)
                count++;

    cout << count << endl;

    f.close();
    return 0;
}