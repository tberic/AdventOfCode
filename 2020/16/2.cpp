#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>

using namespace std;

int in_range(int x, int a1, int b1, int a2, int b2)
{
    return ( (x >= a1 && x <= b1) || (x >= a2 && x <= b2) );
}

int main()
{
    ifstream f, g;
    f.open("input.txt");
    g.open("valid.txt");
    string line;
    vector<int> my_ticket, ticket;
    vector<string> fields;
    vector<int> start1, start2, end1, end2;
    vector< list<int> > possible_fields;

    while (getline(f, line))
    {
        if (line == "")
            break;
        string s = line.substr(0, line.find(":"));
        fields.push_back(s);
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

    for (int i = 0; i < start1.size(); ++i)
    {
        list<int> l;
        for (int j = 0; j < start1.size(); ++j)
            l.push_back(j);
        possible_fields.push_back(l);
    }

    getline(f, line); //your ticket
    getline(f, line);

    istringstream is(line);
    int x;
    char c;
    while (is >> x)
    {
        //cout << x << " ";
        my_ticket.push_back(x);
        is >> c;
    }
    f.close();

    // first pass: remove the fields which are not possible
    while (!g.eof())
    {
        getline(g, line);
        istringstream is(line);
        //cout << line << ": ";
        ticket.clear();
        int pos = 0;
        while (is >> x)
        {
            ticket.push_back(x);

            for (int i = 0; i < start1.size(); ++i)
                if ( !in_range(x, start1[i], end1[i], start2[i], end2[i]) )
                {
                    possible_fields[pos].remove(i);
                }           


            pos++;
        }
    }

    // second pass: whittle it down to just one field
    int flag;
    do
    {
        flag = 0;
        for (int i = 0; i < possible_fields.size(); ++i)
            if (possible_fields[i].size() == 1)
            {
                for (int j = 0; j < possible_fields.size(); ++j)
                    if (j != i)
                        possible_fields[j].remove(possible_fields[i].front());                
            }
            else
            {
                flag = 1;
            }
            
    } while (flag);


/*
    for (int i = 0; i < possible_fields.size(); ++i)
    {
        while (!possible_fields[i].empty())
        {
            cout << possible_fields[i].front() << " " << fields[possible_fields[i].front()] << " ";
            possible_fields[i].pop_front();
        }

        cout << endl;
    }
*/

/*
    for (int i = 0; i < ticket.size(); ++i)
        cout << ticket[i] << " ";
    cout << endl;
*/
/*
    for (int i = 0; i < possible_fields.size(); ++i)
    {
        cout << fields[possible_fields[i].front()] << " ";
        if (fields[possible_fields[i].front()].substr(0, 9) == "departure")        
            cout << fields[possible_fields[i].front()] << ": " << my_ticket[possible_fields[i].front()] << endl;
    }
*/

    cout << fields[0] << endl;
    cout << fields[1] << endl;
    cout << fields[2] << endl;
    cout << fields[3] << endl;
    cout << fields[4] << endl;
    cout << fields[5] << endl;

    cout << endl;
    for (int i = 0; i < possible_fields.size(); ++i)
        cout << possible_fields[i].front() << endl;

    g.close();
    return 0;
}