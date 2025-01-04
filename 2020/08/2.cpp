#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int n = 0, acc;
string line[1000];
int visited[1000] = {0};

void reset()
{
    acc = 0;
    for (int i = 0; i < n; ++i)
        visited[i] = 0;
}

int run()
{
    string ins;
    int num, i;

    for (i = 0; !visited[i] && i < n; )
    {
        istringstream is(line[i]);
        is >> ins >> num;

        visited[i] = 1;

        //cout << i << ": " << ins << " " << num << endl;

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

    return (i == n);
}

int main()
{
    ifstream f;
    f.open("input.txt");

    while (getline(f, line[n++]));

    for (int i = 0; i < n; ++i)
    {
        if (line[i].substr(0, 3) == "nop")
        {
            reset();
            line[i].replace(0, 3, "jmp");
            if (run())
                break;
            line[i].replace(0, 3, "nop");
        }        
        else if(line[i].substr(0, 3) == "jmp")
        {
            reset();
            line[i].replace(0, 3, "nop");
            if (run())
                break;
            line[i].replace(0, 3, "jmp");
        }
    }

    cout << acc << endl;

    f.close();
    return 0;
}