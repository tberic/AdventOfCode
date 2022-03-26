#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define MAX 500

int X = MAX/2, Y = MAX/2;
int tile[MAX][MAX] = {{0}}; // 0=white, 1=black
int tile2[MAX][MAX] = {{0}}; // 0=white, 1=black

int flip(int x)
{
    return (x == 0);
}

int black_neighbors(int x, int y)
{
    return tile[x-2][y] + tile[x+2][y] + tile[x-1][y-1] + 
           tile[x+1][y-1] + tile[x-1][y+1] + tile[x+1][y+1];
}

void copy1to2(void)
{
    for (int i = 0; i < MAX; ++i)
        for (int j = 0; j < MAX; ++j)
            tile2[i][j] = tile[i][j];
}

void copy2to1(void)
{
    for (int i = 0; i < MAX; ++i)
        for (int j = 0; j < MAX; ++j)
            tile[i][j] = tile2[i][j];
}

int main()
{
    ifstream f;
    f.open("input.txt");
    string line;
    int xmin = MAX/2, xmax = -MAX/2, ymin = MAX/2, ymax = -MAX/2;

    while (f >> line)
    {
        int i = 0;
        int x = 0, y = 0;
        while (i < line.size())
        {
            if (line.at(i) == 'w')
                x -= 2;
            if (line.at(i) == 'e')
                x += 2;
            if (line.at(i) == 'n')
            {
                i++;
                if (line.at(i) == 'w')
                {
                    x -= 1; y += 1;
                    i++;
                    continue;
                }
                if (line.at(i) == 'e')
                {
                    x += 1; y += 1;
                    i++;
                    continue;
                }
            }
            if (line.at(i) == 's')
            {
                i++;
                if (line.at(i) == 'w')
                {
                    x -= 1; y -= 1;
                    i++;
                    continue;
                }
                if (line.at(i) == 'e')
                {
                    x += 1; y -= 1;
                    i++;
                    continue;
                }
            }
            i++;
        }

        cout << "(" << x << "," << y << ")" << endl;
        tile[X+x][Y+y] = flip(tile[X+x][Y+y]);
        if (x < xmin) xmin = x;
        if (x > xmax) xmax = x;
        if (y < ymin) ymin = y;
        if (y > ymax) ymax = y;
    }   

    for (int day = 1; day <= 100; ++day)
    {
        copy1to2();
        for (int x = xmin-2*day; x <= xmax+2*day; ++x)
            for (int y = ymin-day; y <= ymax+day; ++y)
            {
                int black = black_neighbors(X+x, Y+y);
                
                if (tile[X+x][Y+y] == 1 && (black == 0 || black > 2))
                {
                    tile2[X+x][Y+y] = 0;
                }
                if (tile[X+x][Y+y] == 0 && black == 2)
                {
                    tile2[X+x][Y+y] = 1;
                }
            }
        copy2to1();
    }
/*
    // count the black tiles
    int count = 0;
    for (int x = xmin; x <= xmax; ++x)
        for (int y = ymin; y <= ymax; ++y)
            if (tile[X+x][Y+y] == 1)
                count++;
    cout << count << endl;
*/

    // count the black tiles
    int count = 0;
    for (int x = 0; x < MAX; ++x)
        for (int y = 0; y < MAX; ++y)
            if (tile[x][y] == 1)
                count++;
    cout << count << endl;

    f.close();
    return 0;
}