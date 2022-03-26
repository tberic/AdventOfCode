#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int m = 0, n;
string grid1[100];
string grid2[100];

int valid(int x, int y)
{
    return (x >= 0 && x < m && y >= 0 && y < n);    
}

int occupied(int x, int y)
{
    if ( valid(x, y) )
        return (grid1[x].at(y)=='#');
    return 0;
}

int occupied_neighbors(int x, int y)
{
    return ( occupied(x-1, y-1)+occupied(x-1, y)+occupied(x-1, y+1)+occupied(x, y-1)+
             occupied(x, y+1)+occupied(x+1, y-1)+occupied(x+1, y)+occupied(x+1, y+1) );
}

char change(int i, int j)
{
    if (grid1[i].at(j) == 'L' && occupied_neighbors(i, j) == 0)
        return '#';
    if (grid1[i].at(j) == '#' && occupied_neighbors(i, j)>=4)
        return 'L';
    return grid1[i].at(j);
}

int equal()
{
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            if (grid1[i].at(j) != grid2[i].at(j))
                return 0;
    return 1;
}

int main()
{
    ifstream f;
    f.open("input.txt");

    while (f >> grid1[m++]);
    f.close();
    m--;
    n = grid1[0].size();

    for (int i = 0; i < m; ++i)
        grid2[i] = grid1[i];

    do {
        for (int i = 0; i < m; ++i)
            grid1[i] = grid2[i];

        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                grid2[i].at(j) = change(i, j);
    } while (!equal());

    int sol = 0;
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            if (grid2[i].at(j) == '#')
                sol++;

    cout << sol << endl;

    return 0;
}