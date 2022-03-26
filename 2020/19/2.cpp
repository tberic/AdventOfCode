#include <iostream>
#include <fstream>
#include <string>
#include <regex>

#define MAXN 200

using namespace std;

string rule[MAXN];
int done[MAXN] = {0};
int n = 0;

// s contains only digits and (possibly) spaces
int number(string s)
{
    for (int i = 0; i < s.size(); ++i)    
        if ( s.at(i) < '0' || s.at(i) > '9')
            return 0;
    return 1;
}

string expr(string s)
{
    // trim spaces from beginning and end of the string
    while (s.at(0) == ' ')
        s.erase(0, 1);
    while (s.at(s.size()-1) == ' ')
        s.erase(s.size()-1, 1);
    
    //cout << s << "." << endl;

    if (s.at(0) == '\"') // just a letter
        return s.substr(1, s.size()-2);
    if (number(s)) // just a number
    {
        int x = stoi(s);
        if (done[x])
            return rule[x];
        rule[x] = expr(rule[x]);
        done[x] = 1;
        return rule[x];
    }
    if (s.find("|") != string::npos) // or operator (higher precedence than concatenation)
    {
        string left = s.substr(0, s.find("|"));
        string right = s.substr(s.find("|")+1);

        return string("(") + expr(left) + string(")") + "|" + string("(") + expr(right) + string(")");
    }
    if (s.find(" ") != string::npos) // concatenation
    {
        string left = s.substr(0, s.find(" "));
        string right = s.substr(s.find(" ")+1);
        //cout << left << "..." << right << "." << endl;

        return string("(") + expr(left) + string(")") + string("(") + expr(right) + string(")");
    }

    return "";
}

int main()
{
    ifstream f;
    f.open("input.txt");
    string line, id;

    for (int i = 0; i < MAXN; ++i)
        done[i] = 1;
    // input the rules
    while (1)
    {
        getline(f, line);
        if (line == "")
            break;

        id = line.substr(0, line.find(":"));
        int x = stoi(id);
        line.erase(0, line.find(":")+2);
        rule[x] = line;
        if (x > n) n = x;

        done[x] = 0;
    }
    n++;

    int m = 0;
    string expression[1000];
    while (1)
    {
        getline(f, line);
        if (line == "")
            break;
        expression[m++] = line;
    }

    // careful! updated rules 8 and 11
    // build the regex, first with old rules 8 and 11
    for (int i = 1; i < n; ++i)
        if (!done[i])
        {
            rule[i] = expr(rule[i]);
            done[i] = 1;
            //cout << rule[i] << endl;
        }

    // now we iterate over rules 8 and 11 and build rule 0
    string rule8 = "42";
    string rule11 = "42 31";

    int count = 0;
    for (int i = 0; i < 5; ++i)
    {
        done[8] = 0;
        rule[8] = expr(rule8);
        done[8] = 1;

        rule11 = "42 31";
        for (int j = 0; j < 5; ++j)
        {
            done[11] = 0;
            rule[11] = expr(rule11);
            done[11] = 1;

            rule[0] = expr("8 11");
            //cout << rule[0] << endl;
            regex regex_rule(rule[0]);
            
            for (int k = 0; k < m; ++k)
                if (regex_match(expression[k], regex_rule))
                {
                    count++;
                    //cout << expression[k] << endl;
                }

            rule11 = string("42 ") + rule11 + string(" 31");
        }

        rule8 = string("42 ") + rule8;
    }
    
    

    
    
    cout << count << endl;

    f.close();
    return 0;
}