#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int validate(int a, int b, char c, string pass)
{
    return ( !(pass.at(a) == c) != !(pass.at(b) == c) );
}

int main()
{
    ifstream f;
    f.open("input.txt");
    string password;
    int a, b, n = 0;
    char c, t;

    while (f >> a >> t >> b >> c >> t >> password)
        n += validate(a-1, b-1, c, password);
        
    cout << n << endl;

    f.close();
    return 0;
}