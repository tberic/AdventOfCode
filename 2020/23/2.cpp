#include <iostream>
#include <string>

using namespace std;

long nodes = 1000000L;

struct node
{
    long label;
    struct node *next;
};

void print(node *l)
{
    node *t = l;
    do
    {
        cout << t->label << " ";
        t = t->next;
    } while (t != l);
    cout << endl;
}

long reduce(long x)
{
    if (x > 1)
        return x-1;
    return nodes;
}

int main()
{
    node *start, *current, *temp, *dest;
    string input="158937462"; //"198753462"
    long x;
    node **pos;

    pos = new node*[1000001];

    current = new node;
    current->label = input.at(0)-'0';
    start = current;
    pos[current->label] = current;
    
    for (int i = 1; i < input.size(); ++i)
    {
        temp = new node;
        temp->label = input.at(i)-'0';
        current->next = temp;
        pos[temp->label] = temp;
        current = current->next;

    }
    for (long i = 10; i <= nodes; ++i)
    {
        temp = new node;
        temp->label = i;
        current->next = temp;
        pos[temp->label] = temp;
        current = current->next;
    }
    current->next = start;
    current = current->next;

    long n = 10000000L; //number of rounds
    for (long i = 0; i < n; ++i)
    {
        // remove next three
        start = current->next;
        current->next = current->next->next->next->next;
        
        // find destination
        x = current->label;
        do
        {
            x = reduce(x);

            if ( start->label == x || start->next->label == x || start->next->next->label == x )
                continue;
            dest = pos[x];
            break;
        } while (1);

        // insert removed nodes after destination
        temp = dest;
        dest = temp->next;
        temp->next = start;
        temp->next->next->next->next = dest;
        
        current = current->next;
    }


    cout << pos[1]->next->label << " " << pos[1]->next->next->label << endl;

    //free memory
    for (long i = 0; i < nodes; ++i)
    {
        temp = current;
        current = current->next;
        delete temp;
    }
    delete[] pos;

    return 0;
}