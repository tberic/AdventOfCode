#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <iterator>

using namespace std;

void print(vector<string> v)
{
    for (vector<string>::iterator it = v.begin(); it != v.end(); ++it)
        cout << *it << " ";
    cout << endl;
}

int main()
{
    ifstream f;
    f.open("input.txt");
    string line, word;
    vector<string> ingr;
    map< string, vector<string> > allergens;
    set<string> allergen;
    vector<string> words;

    while (getline(f, line))
    {
        istringstream is(line);
        ingr.clear();
        while (1)
        {
            is >> word;
            if (word.at(0) == '(')
                break;
            ingr.push_back(word);
            words.push_back(word);
        }

        sort(ingr.begin(), ingr.end());

        while (1)
        {
            is >> word;
            string s = word.substr(0, word.size()-1);

            if (allergens.count(s) == 0)
            {
                allergens[s] = ingr;
            }
            else
            {
                vector<string> res;
                sort(allergens[s].begin(), allergens[s].end());
                set_intersection(allergens[s].begin(), allergens[s].end(), 
                                ingr.begin(), ingr.end(), 
                                back_inserter(res));

                allergens[s] = res;
            }

            if (word.at(word.size()-1) == ')')
                break;
        }
    }
    f.close();

    int change = 1;
    while (change)
    {
        change = 0;
        for (map< string, vector<string> >::iterator it = allergens.begin(); it != allergens.end(); ++it)
            if ( (it->second).size() == 1 )
            {
                string name = (it->second)[0];
                for (map< string, vector<string> >::iterator jt = allergens.begin(); jt != allergens.end(); ++jt)
                    if (jt->first != it->first && find((jt->second).begin(), (jt->second).end(), name) != (jt->second).end() )
                    {
                        change = 1;
                        (jt->second).erase( find((jt->second).begin(), (jt->second).end(), name) );
                    }
            }
    }

    for ( map< string, vector<string> >::iterator it = allergens.begin(); it != allergens.end(); ++it )
        allergen.insert((it->second)[0]);
/*
    for (set<string>::iterator it = allergen.begin(); it != allergen.end(); ++it)
        cout << *it << " ";
    cout << endl;
*/
    int count = 0;
    for (vector<string>::iterator it = words.begin(); it != words.end(); ++it)
        if (allergen.find(*it) == allergen.end())
            count++;

    cout << count << endl;

    for ( map< string, vector<string> >::iterator it = allergens.begin(); it != allergens.end(); ++it )
    {
        cout << it->first << ": ";
        print(it->second);
    }

     return 0;
}