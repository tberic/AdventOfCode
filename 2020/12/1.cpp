#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;

void rotate(int &stepx, int &stepy, int deg)
{
    int x, y;
    double rad = deg*M_PI/180;
    x = stepx*cos(rad) - stepy*sin(rad);
    y = stepx*sin(rad) + stepy*cos(rad);
    stepx = x;
    stepy = y;
}

int main()
{
    ifstream f;
    f.open("input.txt");
    string line;
    int x = 0, y = 0;
    int stepx = 1, stepy = 0;

    while (f >> line)
    {
        istringstream is(line.substr(1));
        int n;
        char c = line.at(0);
        is >> n;

//        cout << c << " " << n << endl;

        if (c == 'N') y -= n;
        if (c == 'S') y += n;
        if (c == 'W') x -= n;
        if (c == 'E') x += n;

        if (c == 'L')
            rotate(stepx, stepy, -n);
        if (c == 'R')
            rotate(stepx, stepy, +n);

        if (c == 'F')
        {
            x += stepx*n;
            y += stepy*n;
        }
    }

    cout << abs(x) + abs(y) << endl;

    f.close();
    return 0;
}