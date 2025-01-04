#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <utility>
using namespace std;

#define MAXHEIGHT (10000)

array< array<string, 4>, 4> rocks;
int nRocks = 2022;

void printGrid(array<string, MAXHEIGHT> &grid, int line)
{
    for (int i = line; i >= 0; --i)
        cout << grid[i] << endl;
    cout << endl;
}

bool obstacle(array<string, MAXHEIGHT> &grid, array<string, 4> rock, int x, int y)
{
    bool result = false;
    for (int j = 0; j < 4; ++j)
        for (int k = 0; k < 4; ++k)
            if (rock[j][k] == '#' && grid[y+3-j][x+k] == '#')
                result = true;
    return result;
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout) { return 1; }

    string jet;
    getline(fin, jet);
    int nJet = jet.size();
    int jetIndex = 0;

    array<string, MAXHEIGHT> grid;

    for (int i = 0; i < MAXHEIGHT; ++i)
        grid[i] = string(7, '.');

    rocks[0] = {{"....", "....", "....", "####"}};
    rocks[1] = {{"....", ".#..", "###.", ".#.."}};
    rocks[2] = {{"....", "..#.", "..#.", "###."}};
    rocks[3] = {{"#...", "#...", "#...", "#..."}};
    rocks[4] = {{"....", "....", "##..", "##.."}};

    int line = 0;
    int x, y;
    nRocks = 2022;
    for (int i = 0; i < nRocks; ++i)
    {
        x = 2;
        y = line + 3;

        int rightest = 0, highest = 0;
        for (int j = 0; j < 4; ++j)
            for (int k = 0; k < 4; ++k)
                if (rocks[i % 5][j][k] == '#')
                {
                    rightest = max(rightest, k);
                    highest = max(highest, 3-j);
                }

        // cout << rightest << " " << highest << endl;

        while (1)
        {
            // lateral movement
            if (jet[jetIndex] == '<' && x > 0 && !obstacle(grid, rocks[i % 5], x-1, y))
                    x--;
            else if (jet[jetIndex] == '>' && x + rightest < 6 && !obstacle(grid, rocks[i % 5], x+1, y))
                    x++;
            jetIndex = (jetIndex + 1) % nJet;
            
            // downward movement
            if (y == 0)
                break;

            // bool floor = false;
            // for (int j = 0; j < 4; ++j)
            //     for (int k = 0; k < 4; ++k)
            //         if (rocks[i % 5][j][k] == '#' && grid[y-1+3-j][x+k] == '#')
            //             floor = true;

            if (!obstacle(grid, rocks[i % 5], x, y-1))
                y--;
            else
                break;

            // cout << x << " " << y << endl;
        }

        // place the rock
        for (int j = 0; j < 4; ++j)
            for (int k = 0; k < 4; ++k)
                if (rocks[i % 5][j][k] == '#')
                    grid[y+3-j][x+k] = '#';

        // cout << line << " " << x << " " << y << endl;

        line = max(line, y+highest+1);

        // printGrid(grid, line);
    }

    cout << line << endl;





    fin.close();
    fout.close();
    return 0;
}