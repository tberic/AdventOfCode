#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int main()
{
    ifstream f;
    f.open("input.txt");
    int x, time;
    string word;
    int min = time, id = 0;

    f >> time;

    while (getline(f, word, ','))
    {
        if (word == "x") continue;
        istringstream is(word);
        is >> x;

        if (time % x == 0) 
        {
            min = 0;
            id = x;
        }
        else if (time/x*x + x - time < min)
        {
            min = time/x*x + x - time;
            id = x;
        }
    }

    cout << id*min << endl;

    f.close();
    return 0;
}