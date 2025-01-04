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

map<string, int> pressure;
map<string, vector<string>> passage;
vector<string> names;
vector<string> namesValves;
map<string, int> index;
map<string, int> released{};
array<int, NSTATES> visited{};

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
    
    return state + index[where]*32768;
}

pair<map<string,int>, string> convertFromState(int state)
{
    map<string,int> result;

    for (auto name : namesValves)
        result[name] = 0;

    int where = state / 32768;
    state %= 32768;

    int index = namesValves.size()-1;
    while (state > 0 || index >= 0)
    {
        result[ namesValves[index] ] = state % 2;
        index--;
        state /= 2;
    }

    return make_pair(result, names[where]);
}

void printMap( map<string,int> &released )
{
    for (auto el : released)
        cout << el.first << " " << el.second << endl;
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

    // for (int i = 0; i < visited.size(); ++i)
    //     visited[i] = -1;

    // auto tmp = convertFromState(convertToState("AA"));
    // printMap(tmp.first);
    // cout << tmp.second << endl;

    // released["BB"] = 1;
    // released["DD"] = 1;
    // released["JJ"] = 1;
    // cout << convertToState("DD") << endl;
    // auto tmp = convertFromState(convertToState("DD"));
    // printMap(tmp.first);
    // cout << tmp.second << endl;

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

        if (visited[state] > press)
            continue;
        visited[state] = press+1;

        fout << minute << " "  << name << " " << press << endl;

        if (press + (30-minute)*totalPressureFlow < maxPressure)
            continue;

        if (minute == 30)
        {
            if (press > maxPressure)
                maxPressure = press;
            continue;
        }

        auto par = convertFromState(state);
        released = par.first;
        where = par.second;
        
        if (allReleased())
        {
            int pressureUntilEnd = press + (30-minute) * totalPressureFlow;
            if (pressureUntilEnd > maxPressure)
                maxPressure = pressureUntilEnd;
            continue;
        }

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

    cout << maxPressure << endl;

    fin.close();
    fout.close();
    return 0;
}