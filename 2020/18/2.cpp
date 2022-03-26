/*
    we will modify input.txt by adding parantheses wherever we find '+'
    then we will solve this problem by running 1.exe on the new input
*/

#include <iostream>
#include <fstream>

using namespace std;

string s;

int main()
{
    ifstream f;
    ofstream g;
    f.open("input.txt");
    g.open("output.txt");

    while (getline(f, s))
    {
        int i = 0; 
        while (i < s.size())
        {
            if (s.at(i) != '+')
            {
                i++;
                continue;
            }

            // go left
            int a = i, brackets;
            brackets = 0;
            while ( (s.at(a) < '0' || s.at(a) > '9') && s.at(a) != '(' || brackets > 0)
            {
                a--;
                if (s.at(a) == ')')
                    brackets++;
                if (s.at(a) == '(')
                    brackets--;                
            }
            s.insert(a, "(");

            // go right
            int b = i+1;
            brackets = 0;
            while ( (s.at(b) < '0' || s.at(b) > '9') && s.at(b) != ')' || brackets > 0)
            {
                b++;
                if (s.at(b) == '(')
                    brackets++;
                if (s.at(b) == ')')
                    brackets--;
            }

            s.insert(b+1, ")");
            i += 2;

            //cout << s << endl;
        }
        
        g << s << endl;
    }

    f.close();
    g.close();
    return 0;
}