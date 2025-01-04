#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <utility>
using namespace std;

#define NSTATES (2*64*32768)

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
    int player;

    node() {};
    node(int minutes_, int pressure_, int state_, string pos_, int player_) : 
        minutes(minutes_), pressure(pressure_), state(state_), pos(pos_), player(player_) {};
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

int convertToState(string where, int player)
{
    int state = 0;
    for (auto name : namesValves)
    {
        state *= 2;
        if (released[name])
            state++;
    }

    state *= 2;
    state += player;
    
    return state + index[where]*65536;
}

pair<map<string,int>, string> convertFromState(int state)
{
    map<string,int> result;

    for (auto name : namesValves)
        result[name] = 0;

    int where = state / 65536;
    state %= 65536;

    int player = state % 2;
    state /= 2;

    int index = namesValves.size()-1;
    while (state > 0 || index >= 0)
    {
        result[ namesValves[index] ] = state % 2;
        index--;
        state /= 2;
    }

    return make_pair(result, names[where]);
}

int calcAllReleasedState()
{
    for (auto name : namesValves)
        released[name] = 1;

    int result = convertToState("AA", 1) % 65536;

    for (auto name : namesValves)
        released[name] = 0;
    
    return result;
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
    Q.push( node(0, 0, convertToState("AA", 1), "AA", 0) );

    for (int i = 0; i < visited.size(); ++i)
        visited[i] = -1;

    int allReleasedState = calcAllReleasedState();

    node T;
    int maxPressure = 0;
    while (!Q.empty())
    {
        T = Q.front();
        string name = T.pos;
        int minute = T.minutes;
        int press = T.pressure;
        int state = T.state;
        int player = T.player;
        string where;
        Q.pop();

        if (visited[state] >= press)
            continue;
        visited[state] = press;

        fout << minute << " "  << name << " " << press << " " << player << endl;

        // if (press + (26-minute)*totalPressureFlow < maxPressure)
        //     continue;

        if (minute == 26)
        {
            if (player == 1)
            {
                if (press > maxPressure)
                   maxPressure = press;
                continue;
            }
            else
            {
                player = 1;
                minute = 0;
                name = "AA";
            }
        }

        // if (state % 65536 == allReleasedState && player == 1)
        // {
        //     int pressureUntilEnd = press + (26-minute) * totalPressureFlow;
        //     if (pressureUntilEnd > maxPressure)
        //         maxPressure = pressureUntilEnd;
        //     continue;
        // }

        auto par = convertFromState(state);
        released = par.first;
        where = par.second;

        if (player)
            press += releasedPressure();
        if (pressure[name] > 0 && !released[name])
        {
            released[name] = 1;
            int newState = convertToState(name, player);
            if (press > visited[newState])
                Q.push( node(minute + 1, press, newState, name, player) );
            released[name] = 0;
        }
        
        for (auto el : passage[name])
        {
            int newState = convertToState(el, player);
            if (press > visited[newState])
                Q.push( node(minute + 1, press, newState, el, player) );
        }
    }

    cout << maxPressure << endl;

    fin.close();
    fout.close();
    return 0;
}