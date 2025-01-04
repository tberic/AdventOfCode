#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>

using namespace std;

map<string, string> passport;

void print()
{
    for (map<string, string>::iterator it = passport.begin(); it != passport.end(); it++)    
        cout << it->first << ":" << it->second << endl;

    cout << endl;
}

void reset()
{
    passport.clear();
}

int validate()
{
    return ( (passport.size() == 8) || ((passport.size() == 7) && passport.count("cid") == 0 ) );
}

int main()
{
    ifstream f;
    f.open("input.txt");
    string word, line, key, value;
    int n = 0;

    reset();
    while (getline(f, line))
    {
        if (line.empty())
        {
            n += validate();
            // print();
            reset();
        }
        else
        {
            istringstream iss(line);
            while (iss >> word)
            {
                key = word.substr(0, word.find(":"));
                value = word.substr(word.find(":")+1);
                passport[key] = value;
            }
        }
    }
    n += validate();

    cout << n << endl;
        
    f.close();
    return 0;
}