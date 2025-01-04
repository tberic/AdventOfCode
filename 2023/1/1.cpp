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
    int sum = 0;

    while (getline(fin, line))
    {
        if (line == "")
        {
            continue;
        }

        int first = -1, last = -1;
        for (int i = 0; i < line.length(); ++i)
            if (isdigit(line[i]))
            {
                if (first == -1)
                    first = i;
                last = i;
            }

        // cout << line[first] << line[last] << endl;
        cout << (line[first]-'0')*10 + (line[last]-'0') << endl;
        sum += (line[first]-'0')*10 + (line[last]-'0');
    }

    cout << sum << endl;

    fin.close();
    fout.close();
    return 0;
}