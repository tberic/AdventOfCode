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

    array< array< array<int, MAXDIM>, MAXDIM>, MAXDIM> grid{};

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

    int count = 0;
    for (x = 1; x <= maxx+1; ++x)
        for (y = 1; y <= maxy+1; ++y)
            for (z = 1; z <= maxz+1; ++z)
                if (grid[x][y][z])
                {
                    count += (grid[x-1][y][z] == 0);
                    count += (grid[x+1][y][z] == 0);
                    count += (grid[x][y-1][z] == 0);
                    count += (grid[x][y+1][z] == 0);
                    count += (grid[x][y][z-1] == 0);
                    count += (grid[x][y][z+1] == 0);
                }

    cout << count << endl;

    fin.close();
    fout.close();
    return 0;
}