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

    constexpr int maxGridX = 1000;
    constexpr int maxGridY = 200;

    int minx = maxGridX-1, maxx = 0, miny = maxGridY-1, maxy = 0;
    int lastx, lasty;

    array<array<int, maxGridY>, maxGridX> grid;

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

    for (int i = 0; i < maxGridX; ++i)
        grid[i][maxy+2] = 1;

    int sandStartX = 500, sandStartY = 0;
    int sandX, sandY;
    int countSand = 0;
    bool nowhereToGo = false;    
    
    while (1)
    {
        countSand++;
        sandX = sandStartX;
        sandY = sandStartY;

        // cout << countSand << endl;

        while (1)
        {
            // cout << sandX << ":" << sandY << endl;
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
        if (sandX == sandStartX && sandY == sandStartY)
            break;

        grid[sandX][sandY] = 1;

    // for (int y = 0; y <= maxy+2; ++y)
    // {
    //     for (int x = minx; x <= maxx; ++x)
    //         cout << (grid[x][y] ? "#" : ".");

    //     cout << endl;
    // }

    }
    
    cout << countSand << endl;

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