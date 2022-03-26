#include <iostream>
#include <fstream>
#include <string>

#define N 96

using namespace std;

string pic[N];
string monster[3];

void print(string grid[N])
{
    for (int i = 0; i< N; ++i)
        cout << grid[i] << endl;
    cout << endl;
}

void rotate(string A[N])
{
    string B[N];

    for (int i = 0; i < N; ++i)
        B[i] = string(N, '.');

    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            B[N-1-j].at(i) = A[i].at(j);
    
    for (int i = 0; i < N; ++i)
        A[i] = B[i];
}

void hflip(string grid[N])
{
    for (int i = 0; i < N/2; ++i)
    {
        string t;
        t = grid[i];
        grid[i] = grid[N-i-1];
        grid[N-i-1] = t;
    }
}

void vflip(string grid[N])
{
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N/2; ++j)
        {
            char t;
            t = grid[i].at(j);
            grid[i].at(j) = grid[i].at(9-j);
            grid[i].at(9-j) = t;
        }
    }
}

void find_monster(void)
{
    for (int i = 0; i < N-2; ++i)
        for (int j = 0; j < N-monster[0].size()+1; ++j)
        {
            int t = 1;
            for (int k = 0; k < 3; ++k)
                for (int l = 0; l < monster[k].size(); ++l)
                    if ( monster[k].at(l) == '#' && pic[i+k].at(j+l) != '#' )
                        t = 0;                        

            if (t)
            {
                //cout << i << " " << j << endl;
                for (int k = 0; k < 3; ++k)
                    for (int l = 0; l < monster[k].size(); ++l)
                        if ( monster[k].at(l) == '#' )
                            pic[i+k].at(j+l) = 'O';
            }
        }
}

int main()
{
    ifstream f;
    f.open("picture.txt");

    for (int i = 0; i < N; ++i)
        getline(f, pic[i]);

    // remember to check other rotations and orientations
    monster[0] = "                  # ";
    monster[1] = "#    ##    ##    ###";
    monster[2] = " #  #  #  #  #  #   ";

    
    hflip(pic); rotate(pic);
    find_monster();

    int count = 0;
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            count += (pic[i][j] == '#');
    cout << count << endl;

    print(pic);

    f.close();
    return 0;
}