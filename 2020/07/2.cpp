#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

#define MAXN 600

map<string, int> color;
int a[MAXN][MAXN] = {{0}};
int n = 0;
int visited[MAXN] = {0};

long DFS(int x)
{
    long sum = 0;
    for (int i = 0; i < n; ++i)
        if (a[x][i])
        {
            sum += a[x][i]*(1+DFS(i));
        }
    return sum;
}

int main()
{
    ifstream f;
    f.open("input.txt");
    string line;

    while (getline(f, line))
    {
        string s = line.substr(0, line.find("bags")-1);
        color[s] = n++;
    }
    f.close();

    f.open("input.txt");
    while (getline(f, line))
    {
        string s = line.substr(0, line.find("bags")-1);

        //cout << s << ": ";

        int pos = line.find("contain") + 7;
        if ( line.substr(pos) == " no other bags." )
        {
            //cout << s << "  no other bags" << endl; 
            continue;
        }
        pos--;
        do
        {
            pos+=2;
            char c = line.at(pos);
            pos += 2;
            int pos2 = line.find("bag", pos);
            string t = line.substr(pos, pos2-pos-1);
            //cout << t << ". ";

            a[color[s]][color[t]] = c-'0';

            pos += t.size() + 4;
            if (c != '1') pos++;            
        } while (line.at(pos) == ',');
    }
/*
    for (int k = 0; k < n; ++k)
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if (a[i][k] && a[k][j])
                    a[i][j] = a[i][k]+a[k][j];
*/

    long count = DFS(color["shiny gold"]);
/*
    int count = 0;
    for (int i = 0; i < n; ++i)
        count += a[i][color["shiny gold"]];
*/
    cout << count << endl;

    f.close();
    return 0;
}