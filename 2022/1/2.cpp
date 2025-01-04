#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout)
    {
        return 1;
    }

    string line;
    int currentCalories = 0;
    vector<int> calories;

    while (getline(fin, line))
    {
        if (line == "")
        {
            calories.push_back(currentCalories);
            currentCalories = 0;
            continue;
        }
        
        int x = stoi(line);
        currentCalories += x;
    }

    sort(calories.begin(), calories.end(), greater<>());
    cout << calories[0] + calories[1] + calories[2] << endl;

    fin.close();
    fout.close();
    return 0;
}