#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct node
{
    // node() {};
    node(string nameVal, node *parentVal = nullptr) : 
        name(nameVal), parent(parentVal), children(), size(0) {};
    
    string name;
    vector<node*> children;
    int size;
    node *parent;
};

int traverse(node *n)
{
    if (n == nullptr)
        return 0;
    
    for (int i = 0; i < n->children.size(); i++)
        n->size += traverse(n->children[i]);

    cout << n->name << ": " << n->size << endl;

    return n->size;
}

void find_nodes(node *n, vector<int> &sizes)
{
    sizes.push_back(n->size);
    
    for (int i = 0; i < n->children.size(); i++)
        find_nodes(n->children[i], sizes);
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout)
    {
        return 1;
    }

    node *root = nullptr, *pos = nullptr;
    root = new node("/");

    string line;
    vector<string> lines;

    while (getline(fin, line))
        lines.push_back(line);

    int i = 0;
    while (i < lines.size())
    {
        // cout << i << ": ";
        line = lines[i];
        // cout << line << endl;
        
        stringstream in(line);
        char c;
        string op, name;        

        if (line[2] == 'c' && line[3] == 'd')
        {
            in >> c >> op >> name;
            // cout << c << ":" << op << ":" << name << endl;

            if (name == "/")
                pos = root;
            else if (name == "..")
                pos = pos->parent;
            else
            {
                int k;
                for (k = 0; k < pos->children.size(); ++k)
                    if (pos->children[k]->name == name)
                        break;
                pos = pos->children[k];
            }
        }
        else if (line[2] == 'l' && line[3] == 's')
        {
            int j = i+1;
            while (j < lines.size() && lines[j][0] != '$')
            {
                string s;
                int x;
                // cout << lines[j] << endl;
                if (isdigit(lines[j][0]))
                {
                    stringstream fileData(lines[j]);
                    fileData >> x >> s;
                    pos->size += x;
                }
                else
                {
                    stringstream fileData(lines[j]);
                    fileData >> s >> name;
                    pos->children.push_back(new node(name, pos));
                }
                j++;
            }
            i = j-1;
        }

        ++i;
    }

    traverse(root);

    vector<int> sizes;
    find_nodes(root, sizes);
    sort(sizes.begin(), sizes.end());

    int unusedSpace = 70000000 - root->size;
    int toFree = 30000000 - unusedSpace;
    // cout << toFree << endl;

    for (auto x : sizes)
        if (x > toFree)
        {
            cout << x << endl;
            break;
        }

    fin.close();
    fout.close();
    return 0;
}