#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int priority(char c)
{
    if (c >= 'a' && c <= 'z')
        return c - 'a' + 1;
    if (c >= 'A' && c <= 'Z')
        return c - 'A' + 27;
    return 0;
}

char find_common2(string first, string second)
{
    for (auto c : first)
        if (second.find(c) != string::npos)
            return c;
}

char find_common3(string first, string second, string third)
{
    for (auto c : first)
        if (second.find(c) != string::npos && third.find(c) != string::npos)
            return c;
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
    int score = 0;
    while (getline(fin, line))
    {
        string group[3] = {};
        group[0] = line;
        getline(fin, line);
        group[1] = line;
        getline(fin, line);
        group[2] = line;

        char common = find_common3(group[0], group[1], group[2]);
        score += priority(common);
    }

    cout << score << endl;

    fin.close();
    fout.close();
    return 0;
}