#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <utility>
#include <algorithm>
using namespace std;

#define NSTATES (32768)
#define MAXN (64)
#define INF (100000)

map<string, int> pressure;
map<string, int> valveState;
map<string, vector<string>> passage;
vector<string> names;
vector<string> namesValves;
map<string, int> index;
map<string, int> released{};
array<int, NSTATES> cost{};
array<array<int, MAXN>, MAXN> A{};

void visit(string where, int minute, int state, int flow)
{
    if (flow > cost[state])
        cost[state] = flow;

    for (auto el : namesValves)
    if (minute - A[index[where]][index[el]] - 1 > 0 && !(valveState[el] & state))
    {
        visit(el, minute - A[index[where]][index[el]] - 1, state | valveState[el], 
        flow + (minute - A[index[where]][index[el]] - 1) * pressure[el]);
    }
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout) { return 1; }

    string line;
    string start, tunnel;
    int press;
    int nCaves = 0;
    while (getline(fin, line))
    {
        stringstream in(line);
        in >> start >> press;

        names.push_back(start);
        if (press > 0)
        {            
            namesValves.push_back(start);
        }
        pressure[start] = press;
        index[start] = nCaves;

        while (in >> tunnel)
        {
            passage[ start ].push_back( tunnel );
        }

        nCaves++;
    }

    for (int i = 0; i < namesValves.size(); ++i)
        valveState[namesValves[i]] = 1<<i;

    for (int i = 0; i < nCaves; ++i)
        for (int j = 0; j < nCaves; ++j)
            if (find( passage[names[i]].begin(), passage[names[i]].end(), names[j]) != passage[names[i]].end() )
                A[i][j] = 1;
            else
                A[i][j] = INF;

    // Floyd-Warshall
    for (int k = 0; k < nCaves; ++k)
        for (int i = 0; i < nCaves; ++i)
            for (int j = 0; j < nCaves; ++j)
                if (A[i][k] + A[k][j] < A[i][j])
                    A[i][j] = A[i][k] + A[k][j];


    for (int i = 0; i < cost.size(); ++i)
        cost[i] = 0;


    visit("AA", 26, 0, 0);

    int maxPressure = 0;
    for (int i = 0; i < NSTATES; ++i)
        for (int j = 0; j < NSTATES; ++j)
            if (!(i & j) && cost[i] + cost[j] > maxPressure)
                maxPressure = cost[i] + cost[j];

    cout << maxPressure << endl;

    // for (int i = 0; i < NSTATES; ++i)
    //     fout << cost[i] << endl;

    fin.close();
    fout.close();
    return 0;
}