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

vector<string> grid;
int x, y;
int m, n;

void moveRight()
{
    int x1 = (x + 1) % n;
    if ( grid[y][x1] == '#')
        return ;
    while ( grid[y][x1] == ' ')
        x1 = (x1 + 1) % n;
    if (grid[y][x1] == '#')
        return ;
    x = x1;
}

void moveLeft()
{
    int x1 = (x + n - 1) % n;
    if ( grid[y][x1] == '#')
        return ;
    while ( grid[y][x1] == ' ')
        x1 = (x1 + n - 1) % n;
    if (grid[y][x1] == '#')
        return ;
    x = x1;
}

void moveDown()
{
    int y1 = (y + 1) % m;
    if ( grid[y1][x] == '#')
        return ;
    while ( grid[y1][x] == ' ')
        y1 = (y1 + 1) % m;
    if (grid[y1][x] == '#')
        return ;
    y = y1;
}

void moveUp()
{
    int y1 = (y + m - 1) % m;
    if ( grid[y1][x] == '#')
        return ;
    while ( grid[y1][x] == ' ')
        y1 = (y1 + m - 1) % m;
    if (grid[y1][x] == '#')
        return ;
    y = y1;
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout) { return 1; }

    string line;
    n = 0;
    while (getline(fin, line))
    {
        grid.push_back(line);
        if (line.length() > n)
            n = line.length();
    }

    string password = grid[grid.size()-1];
    grid.pop_back();
    grid.pop_back();
    m = grid.size();

    int startX = grid[0].find('.'), startY = 0;

    for (int i = 0; i < m; ++i)
    {
        // replace(lines[i].begin(), lines[i].end(), ' ', '#');
        grid[i].append( n - grid[i].length(), ' ' );
    }

    int dir = 0; // we start facing right
    x = startX, y = startY;

    int i = 0;
    while (i < password.length())
    {
        if (password[i] == 'R')
        {
            dir = (dir + 1) % 4;
            i++;
            continue;
        }
        if (password[i] == 'L')
        {
            dir = (dir + 3) % 4;
            i++;
            continue;
        }
        
        string num = "";
        while (i < password.length() && password[i] >= '0' && password[i] <= '9')
            num += password[i++];

        int steps;
        stringstream in(num);
        in >> steps;

        switch (dir)
        {
            case 0:
                for (int j = 0; j < steps; ++j)
                    moveRight();
                break;
            case 1:
                for (int j = 0; j < steps; ++j)
                    moveDown();
                break;
            case 2:
                for (int j = 0; j < steps; ++j)
                    moveLeft();
                break;
            case 3:
                for (int j = 0; j < steps; ++j)
                    moveUp();
                break;
        }        
    }

    cout << x << " " << y << " " << dir << endl;
    cout << 1000 * (y+1) + 4 * (x+1) + dir << endl;
    
    fin.close();
    fout.close();
    return 0;
}