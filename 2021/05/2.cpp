#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

int grid[1001][1001];

int sign(int x)
{
    if (x > 0)
        return 1;
    if (x < 0)
        return -1;
    return 0;
}

int main()
{
    ifstream f("input.txt");
    string line;    
    int dirx, diry;

    for (int i = 0; i <= 1000; ++i)
        for (int j = 0; j <= 1000; ++j)
            grid[i][j] = 0;

    while (getline(f, line))
    {
        stringstream s(line);
        int x1, y1, x2, y2;
        char c;
        s >> x1 >> c >> y1 >> c >> c >> x2 >> c >> y2;

        //cout << x1 << " " << y1 << " " << x2 << " " << y2 << endl;

        dirx = sign(x2-x1);
        diry = sign(y2-y1);

        for (int x = x1, y = y1; x != x2 || y != y2; x += dirx, y += diry)
            grid[x][y]++;
        grid[x2][y2]++;
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