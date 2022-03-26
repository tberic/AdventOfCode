#include <iostream>
#include <fstream>
#include <string>
#include <stack>
using namespace std;

int main()
{
    ifstream f("input.txt");
    string line;
    stack<char> S;
    string open = "([{<";
    string closed = ")]}>";
    size_t pos1, pos2;
    int sum = 0;
    int score[4] = { 3, 57, 1197, 25137 };
    
    while (getline(f, line))
    {
        S = stack<char>();
        for (int i = 0; i < line.length(); ++i)
        {
            if (open.find(line[i]) != string::npos)
            {   
                S.push(line[i]);
            }
            else if ( (pos1=closed.find(line[i])) != string::npos)
            {
                if (S.empty())
                {
                    sum += score[pos2];
                    break;
                }
                char ch = S.top();
                pos2=open.find(ch);
                if (pos1 != pos2)
                {
                    sum += score[pos1];
                    break;
                }
                else
                    S.pop();
            }
            //cout << S.top() << endl;
        }
    }

    cout << sum << endl;

    f.close();
    return 0;
}