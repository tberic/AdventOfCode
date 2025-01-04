#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <utility>
#include <algorithm>
using namespace std;

#define MAXN (500)

array<string, MAXN> grid;
array<array<int, MAXN>, MAXN> dir{};
int offsetX = 250;
int offsetY = 250;
int m, n;
int minX, minY;
int maxX, maxY;

int printState()
{
    for (int y = minY; y <= maxY; ++y)
    {
        for (int x = minX; x <= maxX; ++x)
            cout << grid[y][x];
        cout << endl;
    }
    cout << endl;
}

void removeCollision(int y, int x)
{
    if (grid[y][x] != 'o')
        return ;
    grid[y][x] = '.';
    if (dir[y+1][x] == 0)
        grid[y+1][x] = '#';
    if (dir[y-1][x] == 1)
        grid[y-1][x] = '#';
    if (dir[y][x+1] == 2)
        grid[y][x+1] = '#';
    if (dir[y][x-1] == 3)
        grid[y][x+1] = '#';
}

void updateCell(int y, int x)
{
    if (dir[y][x] == 0 && grid[y-1][x-1] != '#' && grid[y-1][x] != '#' && grid[y-1][x+1] != '#')
    {
        if (grid[y-1][x] == '.')
            grid[y-1][x] = '0';
        else
            grid[y-1][x]++;
    }
    else if (dir[y][x] == 1 && grid[y+1][x-1] != '#' && grid[y+1][x] != '#' && grid[y+1][x+1] != '#')
    {
        if (grid[y+1][x] == '.')
            grid[y+1][x] = '0';
        else
            grid[y+1][x]++;
    }
    else if (dir[y][x] == 2 && grid[y-1][x-1] != '#' && grid[y][x-1] != '#' && grid[y+1][x-1] != '#')
    {
        if (grid[y][x-1] == '.')
            grid[y][x-1] = '0';
        else
            grid[y][x-1]++;
    }
    else if (dir[y][x] == 3 && grid[y-1][x+1] != '#' && grid[y][x+1] != '#' && grid[y+1][x+1] != '#')
    {
        if (grid[y][x+1] == '.')
            grid[y][x+1] = '0';
        else
            grid[y][x+1]++;
    }
}

int someoneNear(int y, int x)
{
    return (grid[y-1][x-1] == '#' || grid[y-1][x] == '#' || grid[y-1][x+1] == '#' || 
            grid[y][x-1] == '#' ||                           grid[y][x+1] == '#' || 
            grid[y+1][x-1] == '#' || grid[y+1][x] == '#' || grid[y+1][x+1] == '#');
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout) { return 1; }

    string line;    
    m = 0;
    while (getline(fin, line))
    {
        grid[offsetY + m] = line;
        m++;
    }
    n = line.size();

    int padding = (MAXN - n) / 2;
    offsetX = padding;
    for (int i = 0; i < grid.size(); ++i)
    {
        grid[i] = string(padding, '.') + grid[i] + string(padding, '.');
    }

    int nRounds = 10;
    minX = offsetX;
    minY = offsetY;
    maxX = offsetX + n - 1;
    maxY = offsetY + m - 1;

    // cout << minX << " " << minY << " " << maxX << " " << maxY << endl;
    for (int i = 0; i < nRounds; ++i)
    {
        for (int y = minY; y <= maxY; ++y)
            for (int x = minX; x <= maxX; ++x)
                if (grid[y][x] == '#' && someoneNear(y, x))
                    updateCell(y, x);

        printState();

        for (int y = minY-1; y <= maxY+1; ++y)
            for (int x = minX-1; x <= maxX+1; ++x)
                if (grid[y][x] == '#')
                {
                    if (dir[y][x] == 0 && grid[y-1][x] == '0')
                        grid[y][x] = '.';
                    if (dir[y][x] == 1 && grid[y+1][x] == '0')
                        grid[y][x] = '.';
                    if (dir[y][x] == 2 && grid[y][x-1] == '0')
                        grid[y][x] = '.';
                    if (dir[y][x] == 3 && grid[y][x+1] == '0')
                        grid[y][x] = '.';

                    dir[y][x] = (dir[y][x] + 1) % 4;
                }

        for (int y = minY-1; y <= maxY+1; ++y)
            for (int x = minX-1; x <= maxX+1; ++x)
                if (grid[y][x] == '0')
                    grid[y][x] = '#';
                else if (grid[y][x] > '0' && grid[y][x] <= '9')
                    grid[y][x] = '.';


        //TODO: do the rectangle update better, find a tighter rectangle
        minX--; minY--;
        maxX++; maxY++;



    }

    // for (auto line: grid)
    //     cout << line << endl;

    fin.close();
    fout.close();
    return 0;
}