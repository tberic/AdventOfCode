#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <cmath>
using namespace std;

#define MAXHEIGHT (10000)

array< array<string, 4>, 4> rocks;

struct State
{
    int jetStreamIndex;
    int rockIndex;
    array<int, 7> heightOffset;

    State(int jet_, int rock_, array<int, 7> height_) : jetStreamIndex(jet_), rockIndex(rock_), heightOffset(height_) {};

    friend bool operator<(const State &lhs, const State &rhs)
    {
        if (lhs.jetStreamIndex < rhs.jetStreamIndex)
            return true;
        if (lhs.jetStreamIndex == rhs.jetStreamIndex && lhs.rockIndex < rhs.rockIndex)
            return true;
        if (lhs.jetStreamIndex == rhs.jetStreamIndex && lhs.rockIndex == rhs.rockIndex)
        {
            return lhs.heightOffset < rhs.heightOffset;
        }
        return false;
    }

    friend bool operator==(const State &lhs, const State &rhs)
    {
        return (lhs.jetStreamIndex == rhs.jetStreamIndex && lhs.rockIndex < rhs.rockIndex && lhs.heightOffset < rhs.heightOffset);
    }
};

bool obstacle(array<string, MAXHEIGHT> &grid, array<string, 4> rock, int x, int y)
{
    bool result = false;
    for (int j = 0; j < 4; ++j)
        for (int k = 0; k < 4; ++k)
            if (rock[j][k] == '#' && grid[y+3-j][x+k] == '#')
                result = true;
    return result;
}

array<int, 7> topOffsets(array<string, MAXHEIGHT> &grid, int line)
{
    array<int, 7> result{};
    int y;
    for (int x = 0; x < 7; ++x)
    {
        y = line;
        while (y >= 0 && grid[y][x] != '#')
            y--;
        result[x] = line-y;
    }
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

    int line = 0, lastLine = 0;
    int x, y;
    // nRocks = 2022;

    map<State, int> visited;
    vector<int> lines;
    int i = 0;
    int a, b;
    int nRocks = 0;
    while (1)
    {
        x = 2;
        y = line + 3;

        int rightest = 0, highest = 0;
        for (int j = 0; j < 4; ++j)
            for (int k = 0; k < 4; ++k)
                if (rocks[i][j][k] == '#')
                {
                    rightest = max(rightest, k);
                    highest = max(highest, 3-j);
                }

        // cout << rightest << " " << highest << endl;

        while (1)
        {
            // lateral movement
            if (jet[jetIndex] == '<' && x > 0 && !obstacle(grid, rocks[i], x-1, y))
                    x--;
            else if (jet[jetIndex] == '>' && x + rightest < 6 && !obstacle(grid, rocks[i], x+1, y))
                    x++;
            jetIndex = (jetIndex + 1) % nJet;
            
            // downward movement
            if (y == 0)
                break;

            if (!obstacle(grid, rocks[i], x, y-1))
                y--;
            else
                break;
        }

        // place the rock
        for (int j = 0; j < 4; ++j)
            for (int k = 0; k < 4; ++k)
                if (rocks[i][j][k] == '#')
                    grid[y+3-j][x+k] = '#';

        lastLine = line;
        line = max(line, y+highest+1);
        i = (i + 1) % 5;

        lines.push_back(line);

        nRocks++;
        array<int, 7> offsets = topOffsets(grid, line);
        State state(jetIndex, i, offsets);

        if (visited.find(state) != visited.end())
        {
            a = visited[state] - 1;
            b = nRocks - 1;
            cout << nRocks << " " << visited[state] << endl;
            cout << nRocks << " " << jetIndex << " " << i << " ";
            for (int x = 0; x < 7; ++x)
                cout << offsets[x] << ", ";
            cout << endl;
            break;
        }
        visited[state] = nRocks;
    }

    // int a = 140, b = 1875;
    int T = b - a;
    int linesT = lines[b] - lines[a];

    long long N = 1000000000000;

    long long n = floor( double(N - a) / T);
    cout << n << " " << T << " " << linesT << endl;

    cout << N - n * T << endl;

    cout << (long long)n * linesT << endl;

    long long linesFinal = lines[a] + n * linesT + lines[N - n * T] - lines[a];
    cout << linesFinal-1 << endl;


    fin.close();
    fout.close();
    return 0;
}