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

enum 
{
    NORTH = 0,
    SOUTH,
    WEST,
    EAST
};

array<int, 4> flags = {1, 2, 4, 8};

int dirs[4][2] = { {-1, 0}, {+1, 0}, {0, -1}, {0, +1} };

array<string, MAXN> grid;
int startingDir;
int offsetX = 250;
int offsetY = 250;
int m, n;
int minX, minY;
int maxX, maxY;

char print(char c)
{
    if (c < 15)
        return '0' + c;
    return c;
}

int printState()
{
    for (int y = minY; y <= maxY; ++y)
    {
        for (int x = minX; x <= maxX; ++x)
            cout << print(grid[y][x]);
        cout << endl;
    }
    cout << endl;
}

void removeCollision(int y, int x)
{
    if (grid[y][x] > 15)
        return ;

    if (grid[y][x] != 1 && grid[y][x] != 2 && grid[y][x] != 4 && grid[y][x] != 8)
        grid[y][x] = '.';
}

bool nothingInDir(int dir, int y, int x)
{
    if (dir == NORTH && grid[y-1][x-1] != '#' && grid[y-1][x] != '#' && grid[y-1][x+1] != '#')
        return true;
    if (dir == SOUTH && grid[y+1][x-1] != '#' && grid[y+1][x] != '#' && grid[y+1][x+1] != '#')
        return true;
    if (dir == WEST && grid[y-1][x-1] != '#' && grid[y][x-1] != '#' && grid[y+1][x-1] != '#')
        return true;
    if (dir == EAST && grid[y-1][x+1] != '#' && grid[y][x+1] != '#' && grid[y+1][x+1] != '#')
        return true;

    return false;
}

void setCell(int y, int x, int flag)
{
    if (grid[y][x] > 15)
        grid[y][x] = flag;
    else
        grid[y][x] |= flag;
}

void updateCell(int y, int x)
{
    int dir = startingDir;
    int moved = 0;
    while (!moved && dir < startingDir + 4)
    {
        if (nothingInDir(dir%4, y, x))
        {
            setCell(y + dirs[dir%4][0], x + dirs[dir%4][1], flags[dir%4]);
            moved = 1;
        }

        dir++;
    }
}

void moveCell(int y, int x)
{
    if (grid[y][x] > 15)
        return ;

    if (grid[y][x] == 1)
        grid[y+1][x] = '.';
    if (grid[y][x] == 2)
        grid[y-1][x] = '.';
    if (grid[y][x] == 4)
        grid[y][x+1] = '.';
    if (grid[y][x] == 8)
        grid[y][x-1] = '.';

    grid[y][x] = '#';
}

int someoneNear(int y, int x)
{
    return (grid[y-1][x-1] == '#' || grid[y-1][x] == '#' || grid[y-1][x+1] == '#' ||
            grid[y][x-1]   == '#' ||                        grid[y][x+1]   == '#' ||
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

    startingDir = 0;

    // cout << minX << " " << minY << " " << maxX << " " << maxY << endl;
    for (int i = 0; i < nRounds; ++i)
    {
        // cout << "Round " << i+1 << endl;

        for (int y = minY; y <= maxY; ++y)
            for (int x = minX; x <= maxX; ++x)
                if (grid[y][x] == '#' && someoneNear(y, x))
                    updateCell(y, x);

        for (int y = minY-1; y <= maxY+1; ++y)
            for (int x = minX-1; x <= maxX+1; ++x)
                if (grid[y][x] < 16)
                {
                    removeCollision(y, x);
                    moveCell(y, x);
                }

        int minYtmp = maxY + 1;
        int maxYtmp = minY - 1;
        int minXtmp = maxX + 1;
        int maxXtmp = minX - 1;
        
        for (int y = minY - 1; y <= maxY + 1; ++y)
            for (int x = minX - 1; x <= maxX + 1; ++x)
                if (grid[y][x] == '#')
                {
                    minYtmp = min(minYtmp, y);
                    maxYtmp = max(maxYtmp, y);
                    minXtmp = min(minXtmp, x);
                    maxXtmp = max(maxXtmp, x);
                }
        minX = minXtmp;
        maxX = maxXtmp;
        minY = minYtmp;
        maxY = maxYtmp;

        startingDir = (startingDir + 1) % 4;

        // printState();
    }

    int count = 0;
    for (int y = minY; y <= maxY; ++y)
        for (int x = minX; x <= maxX; ++x)
            if (grid[y][x] == '.')
                count++;

    cout << count << endl;

    fin.close();
    fout.close();
    return 0;
}