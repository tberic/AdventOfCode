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

int count(int n)
{
    int sum = 0;
    for (int i = 0; i < 26; ++i)
        sum += (answered[i]==n);
    return sum;
}

int main()
{
    ifstream f;
    f.open("input.txt");
    string line;
    int sum = 0, n = 0;

    while (getline(f, line))
    {
        if (line.empty())
        {
            sum += count(n);
            n = 0;
            reset();            
        }
        else
        {
            for (int i = 0; i < line.size(); ++i)
                answered[line.at(i)-'a']++;
            n++;          
        }
    }

    cout << sum+count(n) << endl;

    f.close();
    return 0;
}