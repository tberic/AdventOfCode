#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <utility>
#include <tuple>
using namespace std;

#define NSTATES (64*64*32768)

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

    node() {};
    node(int pressure_, int minutes_, int state_) : 
        pressure(pressure_), minutes(minutes_), state(state_) {};

    friend bool operator<(const node &lhs, const node &rhs)
    {
        return (lhs.pressure > rhs.pressure);
    }
};

bool allReleased()
{
    for (auto name : namesValves)
        if (!released[name])
            return false;

    return true;
}

int convertToState(string where1, string where2);

int calcAllReleasedState()
{
    for (auto name : namesValves)
        released[name] = 1;

    int result = convertToState("AA", "AA") % 32768;

    for (auto name : namesValves)
        released[name] = 0;
    
    return result;
}

int releasedPressure()
{
    int totalPressure = 0;
    for (auto name : namesValves)
        if (released[name])
            totalPressure += pressure[name];

    return totalPressure;
}

int convertToState(string where1, string where2)
{
    int state = 0;
    for (auto name : namesValves)
    {
        state *= 2;
        if (released[name])
            state++;
    }
    
    return state + (index[where1]*64 + index[where2])*32768;
}

tuple<map<string,int>, string, string> convertFromState(int state)
{
    map<string,int> result;

    for (auto name : namesValves)
        result[name] = 0;

    int where = state / 32768;
    state %= 32768;

    string where1 = names[ where/64 ];
    string where2 = names[ where%64 ];

    int index = namesValves.size()-1;
    while (state > 0 || index >= 0)
    {
        result[ namesValves[index] ] = state % 2;
        index--;
        state /= 2;
    }

    return make_tuple(result, where1, where2);
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
    int totalPressureFlow = 0;
    int nCaves = 0;
    while (getline(fin, line))
    {
        int press;
        stringstream in(line);
        in >> start >> press;

        names.push_back(start);
        if (press > 0)
        {
            namesValves.push_back(start);
            totalPressureFlow += press;
        }
        pressure[start] = press;        
        index[start] = nCaves;

        while (in >> tunnel)
        {
            passage[ start ].push_back( tunnel );
        }

        nCaves++;
    }

    queue<node> Q;
    Q.push( node(0, 0, convertToState("AA", "AA")) );

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
    string name1;
    string name2;
    int minute;
    int press;
    int state;
    string where1;
    string where2;

    for (int i = 0; i < visited.size(); ++i)
        visited[i] = -1;

    int allReleasedState = calcAllReleasedState();

    while (!Q.empty())
    {
        T = Q.front();
        minute = T.minutes;
        press = T.pressure;
        state = T.state;
        Q.pop();

        if (press <= visited[state])
            continue;
        visited[state] = press;

        // fout << minute << " "  << name1 << " " << name2 << " " << press << endl;

        if (press + (26-minute)*totalPressureFlow < maxPressure)
            continue;

        if (minute == 26)
        {
            if (press > maxPressure)
                maxPressure = press;
            continue;
        }

        if (state % 32768 == allReleasedState)
        {
            int pressureUntilEnd = press + (26-minute) * totalPressureFlow;
            if (pressureUntilEnd > maxPressure)
                maxPressure = pressureUntilEnd;
            continue;
        }

        auto tmp = convertFromState(state);
        released = get<0>(tmp);
        name1 = get<1>(tmp);
        name2 = get<2>(tmp);

        press += releasedPressure();

        if (pressure[name1] > 0 && !released[name1])
        {
            released[name1] = 1;
            for (auto el2 : passage[name2])
            {
                int newState = convertToState(name1, el2);
                if (press > visited[newState])
                    Q.push( node(press, minute + 1, newState) );
            }
            released[name1] = 0;
        }
        if (pressure[name2] > 0 && !released[name2])
        {
            released[name2] = 1;
            for (auto el1 : passage[name1])
            {
                int newState = convertToState(el1, name2);
                if (press > visited[newState])
                    Q.push( node(press, minute + 1, newState) );
            }
            released[name2] = 0;
        }
        if (pressure[name1] > 0 && !released[name1] &&
            pressure[name2] > 0 && !released[name2] )
        {
            released[name1] = 1;
            released[name2] = 1;
            int newState = convertToState(name1, name2);
            if (press > visited[newState])
                Q.push( node(press, minute + 1, newState) );
            released[name1] = 0;
            released[name2] = 0;
        }
        
        for (auto el1 : passage[name1])
            for (auto el2 : passage[name2])
            {
                int newState = convertToState(el1, el2);
                if (press > visited[newState])
                    Q.push( node(press, minute + 1, newState) );
            }
    }

    cout << maxPressure << endl;

    fin.close();
    fout.close();
    return 0;
}