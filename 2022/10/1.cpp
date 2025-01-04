#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

int signalStrength(int cycle, int x)
{
    if (cycle == 20 || cycle == 60 || cycle == 100 
    || cycle == 140 || cycle == 180 || cycle == 220)
    {
        cout << ">>> " << cycle << " " << x << endl;
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

            // cout << "noop: " << cycle << " " << x << endl;
        }
        else if (op == "addx")
        {   
            cycle += 1;
            totalSignalStrength += signalStrength(cycle, x);
            cycle += 1;
            totalSignalStrength += signalStrength(cycle, x);
            x += val;

            // cout << "addx: " << cycle << " " << x << endl;
        }
    }

    cout << totalSignalStrength << endl;

    fin.close();
    fout.close();
    return 0;
}