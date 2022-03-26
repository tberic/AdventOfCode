#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    ifstream f("input.txt");
    string line;
    
    while (getline(f, line))
    {

    }

    f.close();
    return 0;
}