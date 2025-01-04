#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

int signalStrength(int cycle, int x)
{
    if (abs((cycle-1) % 40 - x) <= 1)
    {
        cout << "#";
    }
    else
    {
        cout << ".";
    }

    if (cycle % 40 == 0)
        cout << endl;

    if (cycle == 20 || cycle == 60 || cycle == 100 
    || cycle == 140 || cycle == 180 || cycle == 220)
    {
        return cycle * x;
    }
    return 0;
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout)
    {
        return 1;
    }

    string line;
    int cycle = 0, x = 1;
    int totalSignalStrength = 0;
    while (getline(fin, line))
    {
        stringstream in(line);
        string op;
        int val;
        
        in >> op >> val;

        if (op == "noop")
        {
            cycle += 1;
            totalSignalStrength += signalStrength(cycle, x);
        }
        else if (op == "addx")
        {
            cycle += 1;
            totalSignalStrength += signalStrength(cycle, x);
            cycle += 1;
            totalSignalStrength += signalStrength(cycle, x);
            x += val;
        }
    }

    cout << totalSignalStrength << endl;

    fin.close();
    fout.close();
    return 0;
}