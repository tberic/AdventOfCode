#include <iostream>
#include <fstream>

using namespace std;

int X = 10, Y = 10, Z = 10;
int a[50][50][20] = {{{ 0 }}};
int b[50][50][20] = {{{ 0 }}};

int convert(char c)
{
    if (c == '.')
        return 0;
    return 1;
}

int update(int x, int y, int z)
{
    int count = 0;
    for (int i = -1; i < 2; ++i)
        for (int j = -1; j < 2; ++j)
            for (int k = -1; k < 2; ++k)
                count += a[x+i][y+j][z+k];
    count -= a[x][y][z];

    if (a[x][y][z] == 0 && count == 3) 
        return 1;
    if (a[x][y][z] == 1 && (count < 2 || count > 3)) 
        return 0;
    return a[x][y][z];
}

int main()
{
    ifstream f;
    f.open("input.txt");
    int x = 0, y = 0, z = 0;
    int xmin = 0, xmax = 0, ymin = 0, ymax = 0, zmin = 0, zmax = 0;
    string s;

    while (f >> s)
    {
        if (s.size()-1 > ymax) 
            ymax = s.size()-1;
        for (int y = 0; y < s.size(); ++y)
            a[X+x][Y+y][Z+z] = convert(s.at(y));
        x++;
    }
    xmax = x-1;
/*
    for (x = 0; x < 8; ++x)
    {
        for (y = 0; y < 8; ++y)
            cout << a[X+x][Y+y][Z+0];
        cout << endl;
    }
*/

    for (int k = 1; k <= 6; ++k)
    {
        for (x = xmin-k; x <= xmax+k; x++ )
            for (y = ymin-k; y <= ymax+k; y++ )
                for (z = zmin-k; z <= zmax+k; z++ )
                    b[X+x][Y+y][Z+z] = update(X+x, Y+y, Z+z);
 
        for (x = xmin-k; x <= xmax+k; x++ )
            for (y = ymin-k; y <= ymax+k; y++ )
                for (z = zmin-k; z <= zmax+k; z++ )
                    a[X+x][Y+y][Z+z] = b[X+x][Y+y][Z+z];
     }
 
    int count = 0;
    for (x = xmin-7; x <= xmax+7; x++ )
        for (y = ymin-7; y <= ymax+7; y++ )
            for (z = zmin-7; z <= zmax+7; z++ )
                count += a[X+x][Y+y][Z+z];
    cout << count << endl;

    f.close();
    return 0;
}