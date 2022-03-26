#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int check(int grid[5][5])
{
    for (int i = 0; i < 5; ++i)
        if (grid[i][0] == -1 && grid[i][1] == -1 && grid[i][2] == -1 && grid[i][3] == -1 && grid[i][4] == -1)
            return 1;
    for (int i = 0; i < 5; ++i)
        if (grid[0][i] == -1 && grid[1][i] == -1 && grid[2][i] == -1 && grid[3][i] == -1 && grid[4][i] == -1)
            return 1;

    return 0;
}

int sumiraj(int grid[5][5])
{
    int sum = 0;
    for (int i = 0; i < 5; ++i)
        for (int j = 0; j < 5; ++j)
            if (grid[i][j] != -1)
                sum += grid[i][j];
    return sum;
}

int main()
{
    ifstream f("input.txt");
    string line;
    int bingo[1000];
    int card[100][5][5];
    int won[1000] = {0}, nwon = 0;
    int n = 1, m = 0, x;

    getline(f, line);
    stringstream ss(line);
    char c;
    
    ss >> bingo[0];
    while (ss >> c >> x)
        bingo[n++] = x;
/*
    for (int i = 0; i < n; ++i)
        cout << bingo[i] << " ";
*/
    while (getline(f, line))
    {
        for (int i = 0; i < 5; ++i)
        {
            getline(f, line);
            stringstream ss(line);
            for (int j = 0; j < 5; ++j)
                ss >> card[m][i][j];
        }
        m++;
    }

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
            if (!won[j])
            for (int x = 0; x < 5; ++x)
                for (int y = 0; y < 5; ++y)
                    if (card[j][x][y] == bingo[i])
                    {
                        card[j][x][y] = -1;
                        if ( check(card[j]) )
                        {
                            won[j] = 1;
                            nwon++;
                        }

                        if (nwon == m)
                        {
                            int a = sumiraj(card[j]);
                            cout << a*bingo[i] << endl;
                            return 0;
                        }
                    }
    }


    f.close();
    return 0;
}