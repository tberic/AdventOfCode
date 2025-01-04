#include <iostream>
#include <sstream>
#include <string>
#include <deque>
#include <array>
#include <algorithm>
using namespace std;

struct monkey
{
    deque<long long> items;
    string op;
    int test;
    int monkeyTrue;
    int monkeyFalse;
};

int main()
{
    constexpr int nMonkeys = 8;
    array<monkey, nMonkeys> monkeys{};
    array<long long, nMonkeys> inspects{};
    long long mod = 9699690;

    monkeys[0] = { {84, 66, 62, 69, 88, 91, 91}, "old * 11", 2, 4, 7 };
    monkeys[1] = { {98, 50, 76, 99}, "old * old", 7, 3, 6 };
    monkeys[2] = { {72, 56, 94}, "old + 1", 13, 4, 0 };
    monkeys[3] = { {55, 88, 90, 77, 60, 67}, "old + 2", 3, 6, 5 };
    monkeys[4] = { {69, 72, 63, 60, 72, 52, 63, 78}, "old * 13", 19, 1, 7 };
    monkeys[5] = { {89, 73}, "old + 5", 17, 2, 0 };
    monkeys[6] = { {78, 68, 98, 88, 66}, "old + 6", 11, 2, 5 };
    monkeys[7] = { {70}, "old + 7", 5, 1, 3 };

    int nRounds = 10000;
    for (int i = 0; i < nRounds; ++i)
    {
        for (int j = 0; j < nMonkeys; ++j)
        {            
            while (!monkeys[j].items.empty())
            {
                stringstream in(monkeys[j].op);
                string left, op, right;
                in >> left >> op >> right;
                
                long long take = monkeys[j].items.front();
                monkeys[j].items.pop_front();

                inspects[j]++;

                if (op == string("+"))
                {
                    if (right == string("old"))
                    {
                        take *= 2;
                    }
                    else
                    {
                        stringstream rights(right);
                        int val;
                        rights >> val;
                        take += val;
                    }                    
                }
                else if (op == string("*"))
                {
                    if (right == string("old"))
                    {
                        take *= take;
                    }
                    else
                    {
                        stringstream rights(right);
                        int val;
                        rights >> val;
                        take *= val;
                    }

                    take %= mod;
                }

                if (take % monkeys[j].test == 0)
                    monkeys[monkeys[j].monkeyTrue].items.push_back(take);
                else
                    monkeys[monkeys[j].monkeyFalse].items.push_back(take);
            }
        }
    }

    for (int i = 0; i < nMonkeys; ++i)
        cout << inspects[i] << endl;

    sort(inspects.begin(), inspects.end(), greater<int>());
    cout << (long long) inspects[0] * inspects[1] << endl;

    return 0;
}