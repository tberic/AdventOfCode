#include <iostream>
#include <fstream>
#include <sstream>
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
    int x1, x2, y1, y2;
    char c;
    int count = 0;

    while (getline(fin, line))
    {
        stringstream stringin(line);
        stringin >> x1 >> c >> y1 >> c >> x2 >> c >> y2;

        if (x1 > x2)
        {
            swap(x1, x2);
            swap(y1, y2);
        }

        if (x2 > y1)
            continue;
        count++;
    }

    cout << count << endl;

    fin.close();
    fout.close();
    return 0;
}