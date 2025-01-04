#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <array>
#include <utility>
using namespace std;

struct point
{
    point() {};
    point(int stepsVal, int xx, int yy) : steps(stepsVal), x(xx), y(yy) {};
    int x, y, steps;
    friend bool operator<(const point& lhs, const point& rhs)
    {
        return (lhs.steps > rhs.steps);
    }
};

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout)
    {
        return 1;
    }

    vector<string> grid;

    string line;
    int sx, sy, ex, ey, y;
    while (getline(fin, line))
    {
        grid.push_back(line);        
    }
    int m = grid.size();
    int n = grid[0].size();

    for (int x = 0; x < m; ++x)
    {
        y = grid[x].find("S");
        if (y != string::npos)
        {
            sx = x;
            sy = y;
            grid[x][y] = 'a';
        }
        y = grid[x].find("E");
        if (y != string::npos)
        {
            ex = x;
            ey = y;
            grid[x][y] = 'z';
        }
    }

    // Dijkstra
    int inf = 1000000;
    array<array<int, 500>, 500> cost;
    for (int i = 0; i < 500; ++i)
        for (int j = 0; j < 500; ++j)
            cost[i][j] = inf;
    cost[sx][sy] = 0;

    priority_queue< point > PQ;
    PQ.push( point(0, sx, sy) );

    point T;
    while (!PQ.empty())
    {
        T = PQ.top();
        PQ.pop();

        fout << T.steps << " " << T.x << " " << T.y << " " << endl;

        if (T.x == ex && T.y == ey)
        {
            cout << T.steps << endl;
            break;
        }

        if (T.x > 0 && grid[T.x - 1][T.y] - grid[T.x][T.y] <= 1 && cost[T.x - 1][T.y] > T.steps + 1)
        {
            cost[T.x - 1][T.y] = T.steps + 1;
            PQ.push( point(T.steps + 1, T.x - 1, T.y) );
        }
        if (T.x < m-1 && grid[T.x + 1][T.y] - grid[T.x][T.y] <= 1 && cost[T.x + 1][T.y] > T.steps + 1)
        {
            cost[T.x + 1][T.y] = T.steps + 1;
            PQ.push( point(T.steps + 1, T.x + 1, T.y) );
        }
        if (T.y > 0 && grid[T.x][T.y - 1] - grid[T.x][T.y] <= 1 && cost[T.x][T.y - 1] > T.steps + 1)
        {
            cost[T.x][T.y - 1] = T.steps + 1;
            PQ.push( point(T.steps + 1, T.x, T.y - 1) );
        }
        if (T.y < n-1 && grid[T.x][T.y + 1] - grid[T.x][T.y] <= 1 && cost[T.x][T.y + 1] > T.steps + 1)
        {
            cost[T.x][T.y + 1] = T.steps + 1;
            PQ.push( point(T.steps + 1, T.x, T.y + 1) );
        }
    }

    // queue< point > Q;
    // Q.push( point(0, sx, sy) );

    // point T;
    // while (!Q.empty())
    // {
    //     T = Q.front();
    //     Q.pop();

    //     fout << T.steps << " " << T.x << " " << T.y << " " << endl;

    //     if (T.x == ex && T.y == ey)
    //     {
    //         cout << T.steps << endl;
    //         break;
    //     }

    //     if (T.x > 0 && grid[T.x - 1][T.y] - grid[T.x][T.y] <= 1 && cost[T.x - 1][T.y] > T.steps + 1)
    //     {
    //         cost[T.x - 1][T.y] = T.steps + 1;
    //         Q.push( point(T.steps + 1, T.x - 1, T.y) );
    //     }
    //     if (T.x < m-1 && grid[T.x + 1][T.y] - grid[T.x][T.y] <= 1 && cost[T.x + 1][T.y] > T.steps + 1)
    //     {
    //         cost[T.x + 1][T.y] = T.steps + 1;
    //         Q.push( point(T.steps + 1, T.x + 1, T.y) );
    //     }
    //     if (T.y > 0 && grid[T.x][T.y - 1] - grid[T.x][T.y] <= 1 && cost[T.x][T.y - 1] > T.steps + 1)
    //     {
    //         cost[T.x][T.y - 1] = T.steps + 1;
    //         Q.push( point(T.steps + 1, T.x, T.y - 1) );
    //     }
    //     if (T.y < n-1 && grid[T.x][T.y + 1] - grid[T.x][T.y] <= 1 && cost[T.x][T.y + 1] > T.steps + 1)
    //     {
    //         cost[T.x][T.y + 1] = T.steps + 1;
    //         Q.push( point(T.steps + 1, T.x, T.y + 1) );
    //     }
    // }

    // cout << sx << " " << sy << endl;
    // cout << ex << " " << ey << endl;
    // for (int i = 0; i < m; ++i)
    // {
    //     for (int j = 0; j < n; ++j)
    //         cout << grid[i][j];
    //     cout << endl;
    // }

    fin.close();
    fout.close();
    return 0;
}