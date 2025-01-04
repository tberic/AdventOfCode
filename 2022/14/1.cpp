#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <array>
using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout)
    {
        return 1;
    }

    string line, tmp;
    int x, y;
    int minx = 10000, maxx = 0, miny = 10000, maxy = 0;
    int lastx, lasty;

    array<array<int, 200>, 600> grid{};

    while (getline(fin, line))
    {
        stringstream in(line);
        string coords;

        getline(in, coords, ':');
        stringstream inxy(coords);
        inxy >> lastx;
        inxy.ignore();
        inxy >> lasty;
        inxy.ignore();

        minx = (minx > lastx) ? lastx : minx;
        miny = (miny > lasty) ? lasty : miny;
        maxx = (maxx < lastx) ? lastx : maxx;
        maxy = (maxy < lasty) ? lasty : maxy;

        while (getline(in, coords, ':'))
        {
            stringstream inxy(coords);
            inxy >> x;
            inxy.ignore();
            inxy >> y;

            if (x == lastx)
                for (int j = min(lasty, y); j <= max(lasty, y); ++j)
                    grid[x][j] = 1;
            else if (y == lasty)
                for (int i = min(lastx, x); i <= max(lastx, x); ++i)
                    grid[i][y] = 1;

            lastx = x;
            lasty = y;

            minx = (minx > x) ? x : minx;
            miny = (miny > y) ? y : miny;
            maxx = (maxx < x) ? x : maxx;
            maxy = (maxy < y) ? y : maxy;
        }        
    }

    // cout << minx << "-" << maxx << endl;
    // cout << miny << "-" << maxy << endl;

    int sandStartX = 500, sandStartY = 0;
    int sandX, sandY;
    int countSand = 0;

    while (1)
    {
        countSand++;
        sandX = sandStartX;
        sandY = sandStartY;

        while (1)
        {
            if (sandY > maxy)
                break;

            if (!grid[sandX][sandY+1])
                sandY++;
            else if (!grid[sandX-1][sandY+1])
            {
                sandX--;
                sandY++;
            }
            else if (!grid[sandX+1][sandY+1])
            {
                sandX++;
                sandY++;
            }
            else
                break;
        }
        if (sandY > maxy)
            break;

        grid[sandX][sandY] = 1;
    }

    cout << countSand-1 << endl;

    // for (int y = 0; y <= maxy; ++y)
    // {
    //     for (int x = minx; x <= maxx; ++x)
    //         cout << (grid[x][y] ? "#" : ".");

    //     cout << endl;
    // }



    fin.close();
    fout.close();
    return 0;
}