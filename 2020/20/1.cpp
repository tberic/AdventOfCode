#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int n = 0;
string id[200];
string tile[200][10];

void print(string grid[10])
{
    for (int i = 0; i<  10; ++i)
        cout << grid[i] << endl;
    cout << endl;
}

void rotate(string A[10])
{
    string B[10];

    for (int i = 0; i < 10; ++i)
        B[i] = "..........";

    for (int i = 0; i < 10; ++i)
        for (int j = 0; j < 10; ++j)
            B[9-j].at(i) = A[i].at(j);
    
    for (int i = 0; i < 10; ++i)
        A[i] = B[i];
}

void hflip(string grid[10])
{
    for (int i = 0; i < 5; ++i)
    {
        string t;
        t = grid[i];
        grid[i] = grid[9-i];
        grid[9-i] = t;
    }
}

void vflip(string grid[10])
{
    for (int i = 0; i < 10; ++i)
    {
        for (int j = 0; j < 5; ++j)
        {
            char t;
            t = grid[i].at(j);
            grid[i].at(j) = grid[i].at(9-j);
            grid[i].at(9-j) = t;
        }
    }
}

int match_upper_side(int i)
{
    for (int j = 0; j < n; ++j)
        if (j != i)
        {
            for (int k = 0; k < 4; ++k)
            {
                if (tile[i][0] == tile[j][9])
                    return 1;
                rotate(tile[j]);
            }
            
            hflip(tile[j]);
            for (int k = 0; k < 4; ++k)
            {
                if (tile[i][0] == tile[j][9])
                    return 1;
                rotate(tile[j]);
            }

            vflip(tile[j]);
            for (int k = 0; k < 4; ++k)
            {
                if (tile[i][0] == tile[j][9])
                    return 1;
                rotate(tile[j]);
            }
        }

    return 0;
}

int matched_sides(int i)
{
    int sum = 0, max = 0;
    for (int k = 0; k < 4; ++k)
    {
        sum += match_upper_side(i);
        rotate(tile[i]);
    }
    if (sum > max) max = sum;

    hflip(tile[i]);
    sum = 0;
    for (int k = 0; k < 4; ++k)
    {
        sum += match_upper_side(i);
        rotate(tile[i]);
    }
    if (sum > max) max = sum;

    vflip(tile[i]);
    sum = 0;
    for (int k = 0; k < 4; ++k)
    {
        sum += match_upper_side(i);
        rotate(tile[i]);
    }
    if (sum > max) max = sum;

    return max;
}

int main()
{
    ifstream f;
    f.open("input.txt");

    while (!f.eof())
    {
        string line;
        getline(f, line);

        if (line == "")
            break;

        id[n] = line.substr(5, 4);
        //cout << id[n] << endl;

        for (int i = 0; i < 10; ++i)
            getline(f, tile[n][i]);

        n++;
        getline(f, line);
    }

    for (int i = 0; i < n; ++i)
    {
        if (matched_sides(i) == 2)
        cout << i << " " << id[i] << endl;
    }




    f.close();
    return 0;
}