#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int main()
{
    ifstream f;
    f.open("input.txt");
    ofstream g;
    g.open("valid.txt");
    string line;
    vector<int> ticket;
    vector<int> start1, start2, end1, end2;

    while (getline(f, line))
    {
        if (line == "")
            break;
        string s = line.substr(0, line.find(":"));
        istringstream is(line.substr(line.find(":")+1));
        int x;
        char c;
        is >> x; cout << x << "-"; start1.push_back(x);
        is >> c;
        is >> x; cout << x << " | "; end1.push_back(x);
        is >> c; is >> c;
        is >> x; cout << x << "-"; start2.push_back(x);
        is >> c;
        is >> x; cout << x; end2.push_back(x);
        cout << endl;
    }

    getline(f, line); //your ticket
    getline(f, line);

    istringstream is(line);
    int x;
    char c;
    while (is >> x)
    {
        //ticket.push_back(x);
        is >> c;
    }
    cout << endl;

    getline(f, line); //empty line
    getline(f, line); //nearby tickets

    int sum = 0;
    while (!f.eof())
    {
        int valid = 1;
        getline(f, line);
        istringstream is(line);
        ticket.clear();
        while (is >> x)
        {
            ticket.push_back(x);
            is >> c;

            int t = 0;
            for (int i = 0; i < start1.size(); ++i)
                if ( (x < start1[i] || x > end1[1]) && (x < start2[i] || x > end2[1]) )
                    t++;
            
            if (t == start1.size())
            {
                sum += x;
                valid = 0;
            }
        }

        if (valid)
        {
            for (int i = 0; i < ticket.size(); ++i)            
                g << ticket[i] << " ";
            g << endl;
        }
            
    }

    cout << sum << endl;

    f.close();
    g.close();    
    return 0;
}