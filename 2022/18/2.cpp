#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <utility>
using namespace std;

#define MAXDIM (23)

array< array< array<int, MAXDIM>, MAXDIM>, MAXDIM> grid{};

void floodFill(int x, int y, int z, int val)
{
    if (x < 0 || y < 0 || z < 0)
        return ;
    if (x >= MAXDIM || y >= MAXDIM || z >= MAXDIM)
        return ;
    
    if (grid[x][y][z])
        return ;

    grid[x][y][z] = val;
    floodFill(x-1, y, z, val);
    floodFill(x, y-1, z, val);
    floodFill(x, y, z-1, val);
    floodFill(x+1, y, z, val);
    floodFill(x, y+1, z, val);
    floodFill(x, y, z+1, val);
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout) { return 1; }

    string line;
    int x, y, z;
    char c;
    int maxx = 0, maxy = 0, maxz = 0;
    int minx = 10000, miny = 10000, minz = 10000;

    while (getline(fin, line))
    {
        stringstream in(line);
        in >> x >> c >> y >> c >> z;
        grid[x+1][y+1][z+1] = 1;
        maxx = max(x, maxx);
        maxy = max(y, maxy);
        maxz = max(z, maxz);
        minx = min(x, minx);
        miny = min(y, miny);
        minz = min(z, minz);
    }

    cout << minx << "," << miny << "," << minz << endl;
    cout << maxx << "," << maxy << "," << maxz << endl;

    floodFill(0, 0, 0, -1);
    for (x = 1; x <= maxx+1; ++x)
        for (y = 1; y <= maxy+1; ++y)
            for (z = 1; z <= maxz+1; ++z)
                if (grid[x][y][z] == 0)
                    floodFill(x, y, z, 1);


    int count = 0;
    for (x = 1; x <= maxx+1; ++x)
        for (y = 1; y <= maxy+1; ++y)
            for (z = 1; z <= maxz+1; ++z)
                if (grid[x][y][z] == 1)
                {
                    count += (grid[x-1][y][z] == -1);
                    count += (grid[x+1][y][z] == -1);
                    count += (grid[x][y-1][z] == -1);
                    count += (grid[x][y+1][z] == -1);
                    count += (grid[x][y][z-1] == -1);
                    count += (grid[x][y][z+1] == -1);
                }

    cout << count << endl;

    fin.close();
    fout.close();
    return 0;
}