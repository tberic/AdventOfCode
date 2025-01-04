#include <iostream>
#include <fstream>
#include <string>
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
    int maxCalories = 0;
    int currentCalories = 0;
    while (getline(fin, line))
    {
        if (line == "")
        {
            if(currentCalories > maxCalories)
                maxCalories = currentCalories;
            currentCalories = 0;
            continue;
        }
        
        int x = stoi(line);
        currentCalories += x;
    }

    if(currentCalories > maxCalories)
        maxCalories = currentCalories;

    cout << maxCalories << endl;

    fin.close();
    fout.close();
    return 0;
}