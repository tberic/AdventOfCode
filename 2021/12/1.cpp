#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

int main()
{
    ifstream f("input.txt");
    string line;
    
    while (getline(f, line))
    {
        stringstream s(line);
        string a, b;
        s >> a >> c >> b;

    }

    f.close();
    return 0;
}