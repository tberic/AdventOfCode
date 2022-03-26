#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>

using namespace std;

void rotate(int &stepx, int &stepy, int deg)
{
    double x, y;
    double rad = deg*M_PI/180;
    x = stepx*cos(rad) - stepy*sin(rad);
    y = stepx*sin(rad) + stepy*cos(rad);
    //cout << x << " " << y << endl;
    stepx = round(x);
    stepy = round(y);
}

int main()
{
    ifstream f;
    f.open("input.txt");
    string line;
    int x = 0, y = 0;
    int stepx = 10, stepy = 1;

    while (f >> line)
    {
        istringstream is(line.substr(1));
        int n;
        char c = line.at(0);
        is >> n;

        if (c == 'N') stepy += n;
        if (c == 'S') stepy -= n;
        if (c == 'W') stepx -= n;
        if (c == 'E') stepx += n;

        if (c == 'L')
            rotate(stepx, stepy, +n);
        if (c == 'R')
            rotate(stepx, stepy, -n);

        if (c == 'F')
        {
            x += stepx*n;
            y += stepy*n;
        }

        cout << c << ":" << n << " " << "(" << x << "," << y << ") -> " << "(" << stepx << "," << stepy << ")" << endl;
    }

    cout << abs(x) + abs(y) << endl;

    f.close();
    return 0;
}