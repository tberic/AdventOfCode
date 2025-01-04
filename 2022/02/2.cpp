#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int lessThan(int x)
{
    return (x > 1) ? (x-1) : 3;
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout)
    {
        return 1;
    }

    int better[3] = {2, 3, 1};
    int worse[3] = {3, 1, 2};

    string line;
    int score = 0;
    while (getline(fin, line))
    {
        int them = line[0] - 'A';
        int us = line[2] - 'X';

        if (us == 0) // lose
            score += worse[them];
        else if (us == 1) // draw
            score += them + 1 + 3;
        else // win
            score += better[them] + 6;
    }

    cout << score << endl;

    fin.close();
    fout.close();
    return 0;
}