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

char find_common(string first, string second)
{
    for (auto c : first)
        if (second.find(c) != string::npos)
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
        string first = line.substr(0, line.size() / 2);
        string second = line.substr(line.size() / 2);

        char common = find_common(first, second);
        score += priority(common);
    }

    cout << score << endl;

    fin.close();
    fout.close();
    return 0;
}