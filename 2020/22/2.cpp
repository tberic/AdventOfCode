#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <queue>

#define MAXROUNDS 1000

using namespace std;

void print_q(queue<long> q1, queue<long> q2, int n, int r);

long play(queue<long> p1, queue<long> p2, int n);

queue<long> copy(queue<long> q, int n);

long round(queue<long> p1, queue<long> p2, int n, int r);

long score(queue<long> q);

int main()
{
    ifstream f;
    f.open("input.txt");
    string s;
    queue<long> p1, p2;
    long x, n = 0;

    getline(f, s); 
    //Player 1
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
    
    // Player 2
    while (f >> x)
    {
        p2.push(x);
        n++;
    }

    cout << play(p1, p2, 1) << endl;

    f.close();
    return 0;
}


void print_q(queue<long> q1, queue<long> q2, int n, int r)
{
    cout << "Round " << r << " (Game " << n << ")" << endl;
    cout << "Player 1: ";
    while (!q1.empty())
    {
        cout << q1.front() << " ";
        q1.pop();
    }
    cout << endl;
    cout << "Player 2: ";
    while (!q2.empty())
    {
        cout << q2.front() << " ";
        q2.pop();
    }
    cout << endl;
}

long play(queue<long> p1, queue<long> p2, int n)
{
    long r = 1;
    while (!p1.empty() && !p2.empty())
    {
        // vjerojatno je došlo do ponavljanja pozicije
        if (r > MAXROUNDS)
            return 1; 
        
        long x = round(p1, p2, n, r++);
        if (x > 0)
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
    }

    if (p1.empty())
        return -score(p2);
    return score(p1);
}

queue<long> copy(queue<long> q, int n)
{
    queue<long> res;
    while (n--)
    {
        q.pop();
        res.push(q.front());        
    }
    return res;
}

long round(queue<long> p1, queue<long> p2, int n, int r)
{
    // if a position has been repeated

    //print_q(p1, p2, n, r);

    if ( p1.front() < p1.size() && p2.front() < p2.size() )
    {
        queue<long> q1, q2;
        q1 = copy(p1, p1.front());
        q2 = copy(p2, p2.front());        

        return play(q1, q2, n+1);
    }
    else
    {
        if (p1.front() > p2.front())
            return 1;
        else
            return -1;
    }
}

long score(queue<long> q)
{
    long s = 0;
    int n = q.size();
    while (!q.empty())
    {
        s += n*q.front();
        n--;
        q.pop();
    }
    return s;
}