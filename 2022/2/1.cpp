#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout)
    {
        return 1;
    }

    string line;
    int score = 0;
    while (getline(fin, line))
    {
        int them = line[0] - 'A';
        int us = line[2] - 'X';

        score += us + 1;

        if (us == them)
            score += 3;
        else if (us == (them + 1) % 3)
            score += 6;
    }

    cout << score << endl;

    fin.close();
    fout.close();
    return 0;
}