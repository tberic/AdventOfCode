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

#define SIZE (50)

vector<string> grid;
int x, y;
int m, n;

struct Point
{
    int x, y;
    Point(int x_, int y_) : x(x_), y(y_) {};
};

vector<Point> side;
vector<int> right;
vector<int> left;
vector<int> up;
vector<int> down;

int findSide(int x, int y)
{
    for (int i = 0; i < side.size(); ++i)
        if (x >= side[i].x && x < side[i].x + SIZE && 
            y >= side[i].y && y < side[i].y + SIZE)
            return i;
    return 0;
}

Point cubeRight(int x, int y)
{
    int s = findSide(x, y);
    if (x < side[s].x + SIZE)
        x++;
    else
    {
        x = right[s].x;
        y = right[s].y + y;
    }

    return Point(x, y);
}

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


    side.push_back( Point(50, 0) );
    side.push_back( Point(100, 0) );
    side.push_back( Point(50, 50) );
    side.push_back( Point(50, 100) );
    side.push_back( Point(0, 100) );
    side.push_back( Point(0, 150) );

    right.push_back(1);
    right.push_back(3);
    right.push_back(1);
    right.push_back(1);
    right.push_back(3);
    right.push_back(3);
    
    left.push_back(4);
    left.push_back(0);
    left.push_back(4);
    left.push_back(4);
    left.push_back(0);
    left.push_back(0);

    up.push_back(5);
    up.push_back(5);
    up.push_back(0);
    up.push_back(2);
    up.push_back(2);
    up.push_back(4);

    down.push_back(2);
    down.push_back(2);
    down.push_back(3);
    down.push_back(5);
    down.push_back(5);
    down.push_back(1);

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
    
    // for (auto line : lines)
    //     cout << line << endl;

    fin.close();
    fout.close();
    return 0;
}