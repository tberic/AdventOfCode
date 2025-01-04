#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int answered[26] = {0};

void reset()
{
    for (int i = 0; i < 26; ++i)
        answered[i] = 0;
}

int count()
{
    int sum = 0;
    for (int i = 0; i < 26; ++i)
        sum += answered[i];
    return sum;
}

int main()
{
    ifstream f;
    f.open("input.txt");
    string line;
    int sum = 0;

    while (getline(f, line))
    {
        if (line.empty())
        {
            sum += count();
            reset();
        }
        else
        {
            for (int i = 0; i < line.size(); ++i)
                answered[line.at(i)-'a'] = 1;
        }  
    }

    cout << sum+count() << endl;

    f.close();
    return 0;
}