#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <utility>
using namespace std;

using U = long long;

struct Node
{
    char op;
    U val;
    Node *left, *right;

    Node(char op_ = ' ', U val_ = 0, Node *left_ = nullptr, Node *right_ = nullptr) : 
        op(op_), val(val_), left(left_), right(right_) {};
};

struct Data
{
    string left, right;
    char op;
    U val;

    Data(string left_, char op_, string right_) :
        left(left_), op(op_), right(right_) {};
    Data(U val_, char op_) : val(val_), op(op_) {};
    Data() {};

    friend ostream& operator<<(ostream& out, const Data& d)
    {
        if (d.op == ' ')
            out << d.val;
        else
            out << d.left << d.op << d.right;
        return out;
    }
};

map<string, Data> info;

Node *createTree(const Data &d)
{
    Node *n;

    if (d.op == ' ' || d.op == 'X')
    {
        n = new Node(d.op, d.val);
        return n;
    }
    else
    {
        n = new Node(d.op, 0, createTree(info[d.left]), createTree(info[d.right]) );
        return n;
    }   

}

void destroyTree(Node *n)
{
    if (n->left != nullptr)
        destroyTree(n->left);
    if (n->right != nullptr)
        destroyTree(n->right);
    delete n;
}

void traverseTree(Node *n)
{
    if (n == nullptr)
        return ;
    
    if (n->op == ' ')
        cout << n->val;
    else if (n->op == 'X')
        cout << 'x';
    else
    {
        cout << '(';
        traverseTree(n->left);
        cout << n->op;
        traverseTree(n->right);
        cout << ')';
    }
}

U calculate(Node *n)
{
    if (n == nullptr)
        return 0;
    
    if (n->op == ' ')
        return n->val;
    if (n->op == '+')
        return calculate(n->left) + calculate(n->right);
    if (n->op == '-')
        return calculate(n->left) - calculate(n->right);
    if (n->op == '*')
        return calculate(n->left) * calculate(n->right);
    if (n->op == '/')
        return calculate(n->left) / calculate(n->right);

    return 0;
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout) { return 1; }

    string line;
    string name, left, right;
    char op;

    while (getline(fin, line))
    {
        stringstream in(line);
        // in >> name >> left >> op >> right;
        in >> name >> left;
        name = name.substr(0, name.size()-1);
        if (left[0] >= '0' && left[0] <= '9')
        {
            stringstream num(left);
            int val;
            num >> val;
            if (name == "humn")
                info[name] = Data(val, 'X');
            else
                info[name] = Data(val, ' ');
        }        
        else
        {
            in >> op >> right;
            info[name] = Data(left, op, right);
        }
    }

    Node *root = createTree(info["root"]);
    
    // cout << calculate(root->left) << endl;
    // cout << calculate(root->right) << endl;

    traverseTree(root->left); cout << endl << endl << endl;
    cout << calculate(root->right) << endl;

    destroyTree(root);

    // for (auto el : info)
    //     cout << el.first << ": " << el.second << endl;

    fin.close();
    fout.close();
    return 0;
}