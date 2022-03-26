#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <queue>

using namespace std;

void print_q(string s, queue<int> q)
{
    cout << s;
    while (!q.empty())
    {
        cout << q.front() << " ";
        q.pop();
    }
    cout << endl;
}

int main()
{
    ifstream f;
    f.open("input.txt");
    string s;
    queue<int> p1, p2;
    int x, n = 0;

    getline(f, s); //Player 1
    while (s != "")
    {
        getline(f, s);
        if (s == "")
            break;
        istringstream is(s);        
        is >> x;
        p1.push(x);
        n++;
    }
    getline(f, s);

    while (f >> x)
    {
        p2.push(x);
        n++;
    }

    x = 0;
    while (!p1.empty() && !p2.empty())
    {
        x++;
        if (p1.front() > p2.front())
        {
            p1.push(p1.front());
            p1.push(p2.front());
            p1.pop();
            p2.pop();
        }
        else
        {
            p2.push(p2.front());
            p2.push(p1.front());
            p2.pop();
            p1.pop();
        }

        //cout << "Round " << x << ": " << endl;
        //queue<int> q1 = p1, q2 = p2;
        //print_q("Player 1: ", q1);
        //print_q("Player 2: ", q2);
    }


    print_q("Player 1: ", p1);
    print_q("Player 2: ", p2);

    queue<int> q;
    if (!p1.empty()) q = p1;
    if (!p2.empty()) q = p2;

    int score = 0;
    while (!q.empty())
    {
        score += n*q.front();
        n--;
        q.pop();
    }

    cout << score << endl;

    f.close();
    return 0;
}