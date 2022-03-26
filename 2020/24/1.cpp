#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <utility>

using namespace std;

int main()
{
    ifstream f;
    f.open("input.txt");
    string line;
    map<pair<int,int>, int> tile;

    while (f >> line)
    {
        int i = 0;
        int x = 0, y = 0;
        while (i < line.size())
        {
            if (line.at(i) == 'w')
                x -= 2;
            if (line.at(i) == 'e')
                x += 2;
            if (line.at(i) == 'n')
            {
                i++;
                if (line.at(i) == 'w')
                {
                    x -= 1; y += 1;
                    i++;
                    continue;
                }
                if (line.at(i) == 'e')
                {
                    x += 1; y += 1;
                    i++;
                    continue;
                }
            }
            if (line.at(i) == 's')
            {
                i++;
                if (line.at(i) == 'w')
                {
                    x -= 1; y -= 1;
                    i++;
                    continue;
                }
                if (line.at(i) == 'e')
                {
                    x += 1; y -= 1;
                    i++;
                    continue;
                }
            }
            i++;
        }

        cout << "(" << x << "," << y << ")" << endl;
        if (tile.count(make_pair(x, y)) == 0)
        {
            tile[make_pair(x, y)] = 1;
        }
        else
        {
            tile[make_pair(x, y)] = -tile[make_pair(x, y)];
        }
    }   

    int count = 0;
    for (map<pair<int,int>, int>::iterator it = tile.begin(); it != tile.end(); it++)
    {
        if (it->second == 1)
        {
            cout << "(" << (it->first).first << "," << (it->first).second << ")" << endl;
            count++;
        }
    }
    cout << count << endl;

    f.close();
    return 0;
}