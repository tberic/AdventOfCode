#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    ifstream f;
    f.open("input.txt");
    string s[500];
    int i, j, m = 0, n, trees = 0;

    while (f >> s[m++]);
    m--;
    n = s[0].length();

    for (i = 0, j = 0; i < m; ++i)
    {
        if (s[i].at(j) == '#')
            trees++;

        j = (j+3)%n;
    }

    cout << trees << endl;

    f.close();
    return 0;
}