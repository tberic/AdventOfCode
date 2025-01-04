#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <utility>
using namespace std;

struct node
{
    int x;
    struct node *next, *previous;

    node(int x_)
    {
        this->x = x_;
        this->previous = nullptr;
        this->next = nullptr;
    }
};

void moveNodeLeft(node *n)
{
    node *before = n->previous;
    node *after = n->next;

    n->next = before;
    n->previous = before->previous;
    before->next = after;
    before->previous->next = n;
    before->previous = n;
    after->previous = before;
}

void moveNodeRight(node *n)
{
    node *before = n->previous;
    node *after = n->next;

    n->next = after->next;
    n->previous = after;
    after->next->previous = n;
    after->next = n;    
    after->previous = before;
    before->next = after;
}

void printListForward(node *n)
{
    node *stop = n;
    do
    {
        cout << n->x << " ";;
        n = n->next;
    } while (n != stop);
    cout << endl;
}

void printListBackwards(node *n)
{
    node *stop = n;
    do
    {
        cout << n->x << " ";;
        n = n->previous;
    } while (n != stop);
    cout << endl;
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout) { return 1; }

    string line;
    vector<int> list;    
    int x;
    while (getline(fin, line))
    {
        stringstream in (line);
        in >> x;
        list.push_back(x);
    }

    node *start = new node(list[0]), *last = nullptr;
    node *curr = start;
    for (int i = 1; i < list.size(); ++i)
    {
        node *tmp = new node(list[i]);
        curr->next = tmp;
        tmp->previous = curr;
        curr = tmp;
    }
    curr->next = start;
    last = curr;
    start->previous = last;

    vector<node *> position;
    node *nodeZero;

    for (curr = start; curr != last; curr = curr->next)
    {
        position.push_back(curr);
        if (curr->x == 0)
            nodeZero = curr;
    }
    position.push_back(last);

    // printListForward(start);
    // moveNodeRight(start);
    // printListForward(start);

    for (int i = 0; i < list.size(); ++i)
    {
        if (list[i] < 0)
        {
            for (int j = 0; j < -list[i]; ++j) 
                moveNodeLeft(position[i]);
        }
        else
        {
            for (int j = 0; j < list[i]; ++j)
                moveNodeRight(position[i]);
        }

        // printListForward(start);
    }

    curr = nodeZero;
    for (int i = 0; i < 1000; ++i, curr = curr->next);
    cout << curr->x << " ";

    for (int i = 0; i < 1000; ++i, curr = curr->next);
    cout << curr->x << " ";

    for (int i = 0; i < 1000; ++i, curr = curr->next);
    cout << curr->x << " ";




    for (curr = start->next; curr != last; curr = curr->next)
    {
        node *tmp = curr->previous;
        delete tmp;
    }
    delete last;

    fin.close();
    fout.close();
    return 0;
}