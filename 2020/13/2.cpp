#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int main()
{
    ifstream f;
    f.open("input.txt");
    int x[20], offset[20], time, n = 0, off = -1;
    string word;
    int min = time, id = 0;

    f >> time;

    while (getline(f, word, ','))
    {        
        off++;
        if (word == "x") continue;
        istringstream is(word);
        offset[n] = off;
        is >> x[n++];
    }

    for (int i = 0; i < n; ++i)
        cout << offset[i] << ", ";
    cout << endl;

    for (int i = 0; i < n; ++i)
        cout << x[i] << ", ";
    cout << endl;

    f.close();
    return 0;
}