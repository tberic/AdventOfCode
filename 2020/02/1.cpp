#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int validate(int a, int b, char c, string pass)
{
    int x = 0;
    
    for (int i = 0; i < pass.length(); ++i)
        x += (pass.at(i) == c);
        
    return ( (x >= a) && (x <= b) );
}

int main()
{
    ifstream f;
    f.open("input.txt");
    string password;
    int a, b, n = 0;
    char c, t;

    while (f >> a >> t >> b >> c >> t >> password)
        n += validate(a, b, c, password);
        
    cout << n << endl;

    f.close();
    return 0;
}