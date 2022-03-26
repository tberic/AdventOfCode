#include <iostream>
#include <fstream>
#include <string>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ifstream f("input.txt");
    string line;
    stack<char> S;
    string open = "([{<";
    string closed = ")]}>";
    size_t pos1, pos2;
    int score[4] = { 1, 2, 3, 4 };
    int incorrect = 0;
    vector<long long> scores;
    
    while (getline(f, line))
    {
        if (incorrect)
        {
            S = stack<char>();
        }
        else
        {
            long long t = 0;
            while (!S.empty())
            {
                char ch = S.top();
                pos2=open.find(ch);
                t = t*5 + score[pos2];
                S.pop();                
            }
            scores.push_back(t);
        }

        incorrect = 0;
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
                    incorrect = 1;
                    break;
                }
                char ch = S.top();
                pos2=open.find(ch);
                if (pos1 != pos2)
                {
                    incorrect = 1;
                    break;
                }
                else
                    S.pop();
            }
            //cout << S.top() << endl;
        }
    }

    sort(scores.begin(), scores.end());

    cout << scores[scores.size()/2] << endl;

    f.close();
    return 0;
}