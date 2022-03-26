#include <iostream>
#include <string>

using namespace std;

struct node
{
    int label;
    struct node *next;
};

node *find(node *l, int x)
{
    while (l->label != x)
        l = l->next;
    return l;
}

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

int reduce(int x)
{
    if (x > 1)
        return x-1;
    return 9;
}

int main()
{
    node *start, *current, *temp, *dest;
    string input="158937462";
    int x;

    current = new node;
    current->label = input.at(0)-'0';
    start = current;
    
    for (int i = 1; i < input.size(); ++i)
    {
        temp = new node;
        temp->label = input.at(i)-'0';
        current->next = temp;
        current = current->next;
    }
    current->next = start;
    current = current->next;

    int n = 100; //number of rounds
    for (int i = 0; i < n; ++i)
    {
        cout << "Round " << i+1 << ": ";
        print(current);

        // remove next three
        start = current->next;
        current->next = current->next->next->next->next;
        
        // find destination
        x = current->label;
        do
        {
            x = reduce(x);
            //cout << x << " " << start->label << " " << start->next->label << " " << start->next->next->label << " " << endl;

            if ( start->label == x || start->next->label == x || start->next->next->label == x )
                continue;
            dest = find(current, x);            
            break;
        } while (1);

        // insert removed nodes after destination
        temp = dest;
        dest = temp->next;
        temp->next = start;
        temp->next->next->next->next = dest;
        
        current = current->next;
    }


    cout << "Final: ";
    print(find(current, 1));


    //free memory
    for (int i = 0; i < input.size(); ++i)
    {
        temp = current;
        current = current->next;
        delete temp;
    }

    return 0;
}