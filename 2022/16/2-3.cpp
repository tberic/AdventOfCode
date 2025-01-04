#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <utility>
using namespace std;

#define NSTATES (64*32768)
#define REDUCEDSTATES (32768)

map<string, int> pressure;
map<string, vector<string>> passage;
vector<string> names;
vector<string> namesValves;
map<string, int> index;
map<string, int> released{};
array<int, NSTATES> visited{};
array<int, REDUCEDSTATES> cost{};

struct node
{
    int minutes, pressure, state;
    string pos;

    node() {};
    node(int minutes_, int pressure_, int state_, string pos_) :
        minutes(minutes_), pressure(pressure_), state(state_), pos(pos_) {};
};

bool allReleased()
{
    for (auto name : namesValves)
        if (!released[name])
            return false;

    return true;
}

int releasedPressure()
{
    int totalPressure = 0;
    for (auto name : namesValves)
        if (released[name])
            totalPressure += pressure[name];

    return totalPressure;
}

int convertToState(string where)
{
    int state = 0;
    for (auto name : namesValves)
    {
        state *= 2;
        if (released[name])
            state++;
    }

    return state*64 + index[where];
}

map<string,int> convertFromState(int state)
{
    map<string,int> result;

    for (auto name : namesValves)
        result[name] = 0;

    string where = names[state % 64];
    state /= 64;
    
    int index = namesValves.size()-1;
    while (state > 0 || index >= 0)
    {
        result[ namesValves[index] ] = state % 2;
        index--;
        state /= 2;
    }

    return result;
}

void printMap( map<string,int> &released )
{
    for (auto el : released)
        cout << el.first << " " << el.second << endl;
}

int inverted(int x)
{
    return x ^ 0b111111111111111;
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout) { return 1; }

    string line;
    string start, tunnel;
    int press, totalPressureFlow = 0;
    int nCaves = 0;
    while (getline(fin, line))
    {
        stringstream in(line);
        in >> start >> press;

        names.push_back(start);
        if (press > 0)
            namesValves.push_back(start);
        pressure[start] = press;
        totalPressureFlow += press;
        index[start] = nCaves;

        while (in >> tunnel)
        {
            passage[ start ].push_back( tunnel );
        }

        nCaves++;
    }

    queue<node> Q;
    Q.push( node(0, 0, convertToState("AA"), "AA") );

    for (int i = 0; i < visited.size(); ++i)
    {
        visited[i] = -1;
    }

    for (int i = 0; i < cost.size(); ++i)
    {
        cost[i] = 0;
    }

    int allReleasedState = NSTATES-1;

    node T;
    int maxPressure = 0;
    while (!Q.empty())
    {
        T = Q.front();
        string name = T.pos;
        int minute = T.minutes;
        int press = T.pressure;
        int state = T.state;
        string where;
        Q.pop();

        if (visited[state] >= press)
            continue;
        visited[state] = press;

        fout << minute << " "  << name << " " << press << " " << endl;

        if (minute == 26)
        {
            if (press > cost[state / 64])
                cost[state / 64] = press;
            continue;
        }

        released = convertFromState(state);

        press += releasedPressure();
        if (pressure[name] > 0 && !released[name])
        {
            released[name] = 1;
            Q.push( node(minute + 1, press, convertToState(name), name) );
            released[name] = 0;
        }
        
        for (auto el : passage[name])
        {
            Q.push( node(minute + 1, press, convertToState(el), el) );
        }
    }

    maxPressure = 0;
    for (int i = 0; i < REDUCEDSTATES; ++i)
        if (cost[i] + cost[inverted(i)] > maxPressure)
            maxPressure = cost[i] + cost[inverted(i)];

    cout << maxPressure << endl;

    for (int i = 0; i < REDUCEDSTATES; ++i)
        fout << cost[i] << endl;

    fin.close();
    fout.close();
    return 0;
}