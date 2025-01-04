#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <utility>
using namespace std;

struct resources
{
    int ore, clay, obsidian;

    resources(int ore_ = 0, int clay_ = 0, int obsidian_ = 0) : ore(ore_), clay(clay_), obsidian(obsidian_) {};

    friend ostream& operator<<(ostream &out, resources rhs)
    {
        out << rhs.ore << " " << rhs.clay << " " << rhs.obsidian;
        return out;
    }
};

resources parse_input(string s)
{
    s = string(s.begin() + s.find("costs ") + 6, s.end());
    stringstream in(s);
    string word;    

    resources result{};

    int pos = 0;
    int x;
    string type;
    while (s.find("and", pos+1) != string::npos)
    {
        string t = s.substr(pos, pos + s.find("and", pos+1));
        pos = s.find("and", pos+1) + 4;

        stringstream in(t);
        in >> x >> type;
        if (type == "ore")
            result.ore = x;
        if (type == "clay")
            result.clay = x;
        if (type == "obsidian")
            result.obsidian = x;        
    }
    string t = s.substr(pos);
    stringstream inLast(t);
    inLast >> x >> type;
    if (type == "ore")
        result.ore = x;
    if (type == "clay")
        result.clay = x;
    if (type == "obsidian")
        result.obsidian = x;

    return result;
}

array<resources, 4> blueprint;
int maxOre, maxClay, maxObsidian;
int maxGeodeFound = 0;

int geodes(int minute, int ore, int clay, int obsidian, int geode, int oreRobot, int clayRobot, int obsidianRobot, int geodeRobot)
{
    if (minute == 0)
    {
        if (geode > maxGeodeFound)
            maxGeodeFound = geode;
        return geode;
    }

    if (geode + geodeRobot*minute + minute*(minute-1)/2 <= maxGeodeFound)
        return 0;

    ore += oreRobot;
    clay += clayRobot;
    obsidian += obsidianRobot;
    geode += geodeRobot;

    int maxGeode = 0;
    
    if (ore >= blueprint[3].ore && clay >= blueprint[3].clay && obsidian >= blueprint[3].obsidian)
        maxGeode = max(maxGeode, geodes(minute-1, ore-blueprint[3].ore, clay-blueprint[3].clay, obsidian-blueprint[3].obsidian, geode-1, oreRobot, clayRobot, obsidianRobot, geodeRobot+1));
    if (obsidianRobot < maxObsidian && ore >= blueprint[2].ore && clay >= blueprint[2].clay && obsidian >= blueprint[2].obsidian)
        maxGeode = max(maxGeode, geodes(minute-1, ore-blueprint[2].ore, clay-blueprint[2].clay, obsidian-blueprint[2].obsidian-1, geode, oreRobot, clayRobot, obsidianRobot+1, geodeRobot));
    if (clayRobot < maxClay && ore >= blueprint[1].ore && clay >= blueprint[1].clay && obsidian >= blueprint[1].obsidian)
        maxGeode = max(maxGeode, geodes(minute-1, ore-blueprint[1].ore, clay-blueprint[1].clay-1, obsidian-blueprint[1].obsidian, geode, oreRobot, clayRobot+1, obsidianRobot, geodeRobot));
    if (oreRobot < maxOre && ore >= blueprint[0].ore && clay >= blueprint[0].clay && obsidian >= blueprint[0].obsidian)
        maxGeode = max(maxGeode, geodes(minute-1, ore-blueprint[0].ore-1, clay-blueprint[0].clay, obsidian-blueprint[0].obsidian, geode, oreRobot+1, clayRobot, obsidianRobot, geodeRobot));
    // if (ore < maxOre || clay < maxClay || obsidian < maxObsidian)
        maxGeode = max(maxGeode, geodes(minute-1, ore, clay, obsidian, geode, oreRobot, clayRobot, obsidianRobot, geodeRobot));

    return maxGeode;
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout) { return 1; }

    int totalQuality = 0, quality;
    string line;
    while (getline(fin, line))
    {
        int ID, pos;
        string word;
        stringstream in(line);
        in >> word >> ID;
        cout << ID << endl;
        
        pos = line.find('.');
        auto oreRobot = parse_input( string(line.begin() + line.find(':') + 2, line.begin() + pos) );
        auto clayRobot = parse_input( string(line.begin() + pos + 2, line.begin() + line.find('.', pos+1)) );
        pos = line.find('.', pos+1);
        auto obsidianRobot = parse_input( string(line.begin() + pos + 2, line.begin() + line.find('.', pos+1)) );
        pos = line.find('.', pos+1);
        auto geodeRobot = parse_input( string(line.begin() + pos + 2, line.begin() + line.find('.', pos+1)) );

        blueprint[0] = oreRobot;
        blueprint[1] = clayRobot;
        blueprint[2] = obsidianRobot;
        blueprint[3] = geodeRobot;

        maxOre = max(max(oreRobot.ore, clayRobot.ore), max(obsidianRobot.ore, geodeRobot.ore));
        maxClay = obsidianRobot.clay;
        maxObsidian = geodeRobot.obsidian;

        maxGeodeFound = 0;
        quality = geodes(32, 0, 0, 0, 0, 1, 0, 0, 0);
        cout << maxGeodeFound << endl;
        cout << quality << endl;
        totalQuality += ID * quality;
    }

    cout << totalQuality << endl;

    fin.close();
    fout.close();
    return 0;
}