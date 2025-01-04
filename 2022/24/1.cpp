#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
using namespace std;

struct State
{
    int minute, y, x;
    State(int minute_ = 0, int y_ = 0, int x_ = 1) :
        minute(minute_), y(y_), x(x_) {};
    
    friend bool operator<(const State &lhs, const State &rhs)
    {
        return tie(lhs.minute, lhs.y, lhs.x) > tie(rhs.minute, rhs.y, rhs.x);
    }
};

vector<string> grid;
int m, n;
array<vector<int>, 200> rowOffsetsPos;
array<vector<int>, 200> rowOffsetsNeg;
array<vector<int>, 200> columnOffsetsPos;
array<vector<int>, 200> columnOffsetsNeg;

bool isPassable(int minute, int y, int x)
{
    if (grid[y][x] == '#') 
        return false;
    if (grid[y][x] == 'S') 
        return true;
    if (grid[y][x] == 'E') 
        return true;

    for (int i = 0; i < rowOffsetsPos[y].size(); ++i)
        if ( (rowOffsetsPos[y][i] + minute) % n + 1 == x )
            return false;
    for (int i = 0; i < rowOffsetsNeg[y].size(); ++i)
        if ( (rowOffsetsNeg[y][i] + n - minute%n) % n + 1 == x )
            return false;

    for (int i = 0; i < columnOffsetsPos[x].size(); ++i)
        if ( (columnOffsetsPos[x][i] + minute) % m + 1 == y )
            return false;
    for (int i = 0; i < columnOffsetsNeg[x].size(); ++i)
        if ( (columnOffsetsNeg[x][i] + m - minute%m) % m + 1 == y )
            return false;

    return true;
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout) { return 1; }

    string line;
    while (getline(fin, line))
    {
        grid.push_back(line);
    }

    m = grid.size() - 2;
    n = grid[0].size() - 2;
    // find vortices
    for (int i = 1; i <= m; ++i)
        for (int j = 1; j <= n; ++j)
        {
            if (grid[i][j] == '>')
                rowOffsetsPos[i].push_back(j-1);
            if (grid[i][j] == '<')
                rowOffsetsNeg[i].push_back(j-1);
            if (grid[i][j] == 'v')
                columnOffsetsPos[j].push_back(i-1);
            if (grid[i][j] == '^')
                columnOffsetsNeg[j].push_back(i-1);
        }


    priority_queue<State> PQ;
    State s;
    PQ.push( State() );

    set<State> visited{};

    while (!PQ.empty())
    {
        s = PQ.top();
        PQ.pop();

        if (visited.find(s) == visited.end())
            visited.insert(s);
        else
            continue;

        fout << s.minute << " " << s.y << " " << s.x << endl;

        if (s.y == m+1 && s.x == n)
        {
            cout << s.minute << endl;
            break;
        }

        if (s.y > 1 && isPassable(s.minute+1, s.y-1, s.x))
            PQ.push( State(s.minute + 1, s.y - 1, s.x) );
        if (s.y <= m && isPassable(s.minute+1, s.y+1, s.x))
            PQ.push( State(s.minute + 1, s.y + 1, s.x) );
        if (s.x > 1 && isPassable(s.minute+1, s.y, s.x-1))
            PQ.push( State(s.minute + 1, s.y, s.x - 1) );
        if (s.x < n && isPassable(s.minute+1, s.y, s.x+1))
            PQ.push( State(s.minute + 1, s.y, s.x + 1) );
        if (isPassable(s.minute+1, s.y, s.x))
            PQ.push( State(s.minute + 1, s.y, s.x) );
    }

    fin.close();
    fout.close();
    return 0;
}