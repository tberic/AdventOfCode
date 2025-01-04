#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <utility>
#include <algorithm>
#include <cctype>
using namespace std;

int dirs[4][2] = { {0, +1}, {+1, 0}, {0, -1}, {-1, 0} };

enum 
{
    RIGHT = 0,
    DOWN,
    LEFT,
    UP
};

array<vector<string>, 6> grid;
int side, x, y, dir;
int m = 50, n = 50;

bool outOfBounds(int y, int x)
{
    if (y < 0 || x < 0)
        return true;
    if (y >= 50 || x >= 50)
        return true;
    return false;
}

void move()
{
    int newY = y + dirs[dir][0];
    int newX = x + dirs[dir][1];
    int newSide = side;
    int newDir = dir;

    if (outOfBounds(newY, newX))
    {
        if (side == 0)
        {
            switch (dir)
            {
                case RIGHT: newSide = 1; newY = y; newX = 0;
                    break;
                case DOWN: newSide = 2; newY = 0; newX = x;
                    break;
                case LEFT: newSide = 4; newY = 49 - y; newX = 0; newDir = RIGHT;
                    break;
                case UP: newSide = 5; newY = x; newX = 0; newDir = RIGHT;
                    break;
            }
        }
        if (side == 1)
        {
            switch (dir)
            {
                case RIGHT: newSide = 3; newY = 49 - y; newX = 49; newDir = LEFT;
                    break;
                case DOWN: newSide = 2; newY = x; newX = 49; newDir = LEFT;
                    break;
                case LEFT: newSide = 0; newY = y; newX = 49;
                    break;
                case UP: newSide = 5; newY = 49; newX = x;
                    break;
            }
        }
        if (side == 2)
        {
            switch (dir)
            {
                case RIGHT: newSide = 1; newY = 49; newX = y; newDir = UP;
                    break;
                case DOWN: newSide = 3; newY = 0; newX = x;
                    break;
                case LEFT: newSide = 4; newY = 0; newX = y; newDir = DOWN;
                    break;
                case UP: newSide = 0; newY = 49; newX = x;
                    break;
            }
        }
        if (side == 3)
        {
            switch (dir)
            {
                case RIGHT: newSide = 1; newY = 49 - y; newX = 49; newDir = LEFT;
                    break;
                case DOWN: newSide = 5; newY = x; newX = 49; newDir = LEFT;
                    break;
                case LEFT: newSide = 4; newY = y; newX = 49; newDir = LEFT;
                    break;
                case UP: newSide = 2; newY = 49; newX = x;
                    break;
            }
        }
        if (side == 4)
        {
            switch (dir)
            {
                case RIGHT: newSide = 3; newY = y; newX = 0;
                    break;
                case DOWN: newSide = 5; newY = 0; newX = x;
                    break;
                case LEFT: newSide = 0; newY = 49 - y; newX = 0; newDir = RIGHT;
                    break;
                case UP: newSide = 2; newY = x; newX = 0; newDir = RIGHT;
                    break;
            }
        }
        if (side == 5)
        {
            switch (dir)
            {
                case RIGHT: newSide = 3; newY = 49; newX = y; newDir = UP;
                    break;
                case DOWN: newSide = 1; newY = 0; newX = x;
                    break;
                case LEFT: newSide = 0; newY = 0; newX = y; newDir = DOWN;
                    break;
                case UP: newSide = 4; newY = 49; newX = x;
                    break;
            }
        }
    }

    if (grid[newSide][newY][newX] == '#')
        return ;

    side = newSide;
    x = newX; 
    y = newY;
    dir = newDir;
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout) { return 1; }

    string line;
    n = 0;
    int nLine = 0;
    while (nLine < 50 && getline(fin, line))
    {
        line.erase(remove_if(line.begin(), line.end(), ::isspace), line.end());
        grid[0].push_back( line.substr(0, line.size()/2) );
        grid[1].push_back( line.substr(line.size()/2) );
        nLine++;
    }
    
    nLine = 0;
    while (nLine < 50 && getline(fin, line))
    {
        line.erase(remove_if(line.begin(), line.end(), ::isspace), line.end());
        grid[2].push_back( line );
        nLine++;
    }

    nLine = 0;
    while (nLine < 50 && getline(fin, line))
    {
        line.erase(remove_if(line.begin(), line.end(), ::isspace), line.end());
        grid[4].push_back( line.substr(0, line.size()/2) );
        grid[3].push_back( line.substr(line.size()/2) );
        nLine++;
    }

    nLine = 0;
    while (nLine < 50 && getline(fin, line))
    {
        line.erase(remove_if(line.begin(), line.end(), ::isspace), line.end());
        grid[5].push_back( line );
        nLine++;
    }

    getline(fin, line);
    string password;
    getline(fin, password);

    side = 0, y = 0, x = 0, dir = 0;

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

        for (int j = 0; j < steps; ++j)
            move();
    }

    cout << side+1 << " " << y+1 << " " << x+1 << " " << dir << endl;
    cout << 1000 * (y+1) + 4 * (x+1) + dir << endl;
    
    cout << 1000 * 162 + 4 * 38 + dir << endl;

    fin.close();
    fout.close();
    return 0;
}