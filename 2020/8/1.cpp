#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int main()
{
    ifstream f;
    f.open("input.txt");
    string ins;
    int num, n = 0, acc = 0;
    string line[1000];
    int visited[1000] = {0};

    while (getline(f, line[n++]));

    for (int i = 0; !visited[i]; )
    {
        istringstream is(line[i]);
        is >> ins >> num;

        visited[i] = 1;

        cout << i << ": " << ins << " " << num << endl;

        if (ins == "nop")
        {
            i++;
            continue;
        }
        if (ins == "acc")
        {
            acc += num;
            i++;
            continue;
        }
        if (ins == "jmp")
            i += num;            
    }

    cout << acc << endl;

    f.close();
    return 0;
}