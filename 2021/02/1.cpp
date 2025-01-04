#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int main()
{
    ifstream f("input.txt");
    string line, command;
    int pos = 0, depth = 0, x;


    while (getline(f, line))
    {
        stringstream s(line);
        s >> command >> x;

        if (command == "forward")
            pos += x;
        else if (command == "down")
            depth += x;
        else if (command == "up")
            depth -= x;
    }

    cout << pos << " " << depth << endl;
    cout << pos*depth << endl;

    f.close();
    return 0;
}