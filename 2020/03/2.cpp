#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int m = 0, n;
string s[500];

int count_trees(int x, int y)
{
    int i, j, trees = 0;
    for (i = 0, j = 0; i < m; i += y)
    {
        if (s[i].at(j) == '#')
            trees++;

        j = (j+x)%n;
    }

    return trees;
}

int main()
{
    ifstream f;
    f.open("input.txt");
    long trees = 1;
    int x;

    while (f >> s[m++]);
    m--;
    n = s[0].length();

    x = count_trees(1, 1); cout << x << endl; trees *= x;
    x = count_trees(3, 1); cout << x << endl; trees *= x;
    x = count_trees(5, 1); cout << x << endl; trees *= x;
    x = count_trees(7, 1); cout << x << endl; trees *= x;
    x = count_trees(1, 2); cout << x << endl; trees *= x;

    cout << trees << endl;
/*    
    trees *= count_trees(3, 1);
    trees *= count_trees(5, 1);
    trees *= count_trees(7, 1);
    trees *= count_trees(1, 2);

    cout << trees << endl;
*/
    f.close();
    return 0;
}