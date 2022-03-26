#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int n = 0;
string id[200];
string tile[200][10];
int taken[200] = {0};

void print(string grid[10])
{
    for (int i = 0; i<  10; ++i)
        cout << grid[i] << endl;
    cout << endl;
}

void rotate(string A[10])
{
    string B[10];

    for (int i = 0; i < 10; ++i)
        B[i] = "..........";

    for (int i = 0; i < 10; ++i)
        for (int j = 0; j < 10; ++j)
            B[9-j].at(i) = A[i].at(j);
    
    for (int i = 0; i < 10; ++i)
        A[i] = B[i];
}

void hflip(string grid[10])
{
    for (int i = 0; i < 5; ++i)
    {
        string t;
        t = grid[i];
        grid[i] = grid[9-i];
        grid[9-i] = t;
    }
}

void vflip(string grid[10])
{
    for (int i = 0; i < 10; ++i)
    {
        for (int j = 0; j < 5; ++j)
        {
            char t;
            t = grid[i].at(j);
            grid[i].at(j) = grid[i].at(9-j);
            grid[i].at(9-j) = t;
        }
    }
}
/*
int num_of_matches_upper_side(int i)
{
    int sum = 0;
    for (int j = 0; j < n; ++j)
    {
        if (j != i)
        {
            for (int k = 0; k < 4; ++k)
            {
                if (tile[i][0] == tile[j][9])
                {
                    sum += 1;
                    goto next;
                }
                rotate(tile[j]);
            }
            
            hflip(tile[j]);
            for (int k = 0; k < 4; ++k)
            {
                if (tile[i][0] == tile[j][9])
                {
                    sum += 1;
                    goto next;
                }
                rotate(tile[j]);
            }

            vflip(tile[j]);
            for (int k = 0; k < 4; ++k)
            {
                if (tile[i][0] == tile[j][9])
                {
                    sum += 1;
                    goto next;
                }
                rotate(tile[j]);
            }
        }
        next: ;
    }

    return sum;
}
*/

int match_upper_side(int i)
{
    for (int j = 0; j < n; ++j)
        if (j != i && !taken[j])
        {
            for (int k = 0; k < 4; ++k)
            {
                if (tile[i][0] == tile[j][9])
                    return j+1;
                rotate(tile[j]);
            }
            
            hflip(tile[j]);
            for (int k = 0; k < 4; ++k)
            {
                if (tile[i][0] == tile[j][9])
                    return j+1;
                rotate(tile[j]);
            }

            vflip(tile[j]);
            for (int k = 0; k < 4; ++k)
            {
                if (tile[i][0] == tile[j][9])
                    return j+1;
                rotate(tile[j]);
            }
        }

    return 0;
}

int match_lower_side(int i)
{
    for (int j = 0; j < n; ++j)
        if (j != i && !taken[j])
        {
            for (int k = 0; k < 4; ++k)
            {
                if (tile[i][9] == tile[j][0])
                    return j+1;
                rotate(tile[j]);
            }
            
            hflip(tile[j]);
            for (int k = 0; k < 4; ++k)
            {
                if (tile[i][9] == tile[j][0])
                    return j+1;
                rotate(tile[j]);
            }

            vflip(tile[j]);
            for (int k = 0; k < 4; ++k)
            {
                if (tile[i][9] == tile[j][0])
                    return j+1;
                rotate(tile[j]);
            }
        }

    return 0;
}

int equal_right_left(string A[10], string B[10])
{
    for (int i = 0; i < 10; ++i)
        if (A[i].at(9) != B[i].at(0))
            return 0;
    return 1;
}

int match_right_side(int i)
{
    for (int j = 0; j < n; ++j)
        if (j != i && !taken[j])
        {
            for (int k = 0; k < 4; ++k)
            {
                if ( equal_right_left(tile[i], tile[j]) )
                    return j+1;
                rotate(tile[j]);
            }
            
            hflip(tile[j]);
            for (int k = 0; k < 4; ++k)
            {
                if ( equal_right_left(tile[i], tile[j]) )
                    return j+1;
                rotate(tile[j]);
            }

            vflip(tile[j]);
            for (int k = 0; k < 4; ++k)
            {
                if ( equal_right_left(tile[i], tile[j]) )
                    return j+1;
                rotate(tile[j]);
            }
        }

    return 0;
}
/*
int matched_sides(int i)
{
    int sum = 0, max = 0;
    for (int k = 0; k < 4; ++k)
    {
        sum += match_upper_side(i);
        rotate(tile[i]);
    }
    if (sum > max) max = sum;

    hflip(tile[i]);
    sum = 0;
    for (int k = 0; k < 4; ++k)
    {
        sum += match_upper_side(i);
        rotate(tile[i]);
    }
    if (sum > max) max = sum;

    if (max == 2)
        cout << i << " ";

    vflip(tile[i]);
    sum = 0;
    for (int k = 0; k < 4; ++k)
    {
        sum += match_upper_side(i);
        rotate(tile[i]);
    }
    if (sum > max) max = sum;

    if (max == 2)
        cout << i << " ";

    return max;
}
*/
int main()
{
    ifstream f;
    f.open("input.txt");

    while (!f.eof())
    {
        string line;
        getline(f, line);

        if (line == "")
            break;

        id[n] = line.substr(5, 4);
        //cout << id[n] << endl;

        for (int i = 0; i < 10; ++i)
            getline(f, tile[n][i]);

        n++;
        getline(f, line);
    }

/* now we know the corners so we don't have to run this
    for (int i = 0; i < n; ++i)
    {
        if (matched_sides(i) == 2)
        cout << i << " " << id[i] << endl;
    }
*/
    // we don't know the orientation of the corner tiles so we have to check all the starting positions (4! = 24 of them)
    // do we really?
    int corners[4] = {58, 20, 45, 77};
    // we only need one corner and we'll put it upper left and start from there

//    cout << match_right_side(corners[0]) << endl;

    int grid[12][12] = {{0}};
    grid[0][0] = corners[0]; 
    taken[grid[0][0]] = 1;
    for (int i = 1; i < 12; ++i)
    {
        grid[0][i] = match_right_side(grid[0][i-1])-1;
        taken[grid[0][i]] = 1;
    }

    for (int i = 1; i < 12; ++i)
    {
        grid[i][0] = match_lower_side(grid[i-1][0])-1;
        taken[grid[i][0]] = 1;

        //cout << grid[i][0] << endl;
        for (int j = 1; j < 12; ++j)
        {
            grid[i][j] = match_right_side(grid[i][j-1])-1;
            taken[grid[i][j]] = 1;
        }
    }


    for (int i = 0; i < 12; ++i)
    {
        for (int j = 0; j < 12; ++j)
            cout << grid[i][j] << " ";
        cout << endl;
    }

    ofstream g;
    g.open("picture.txt");

    for (int i = 0; i < 12; ++i)
    {
        for (int k = 1; k <= 8; ++k)
        {
            for (int j = 0; j < 12; ++j)
                g << tile[grid[i][j]][k].substr(1, 8);
            g << endl;
        }
    }


/*
    cout << match_right_side(3) << endl;

    print(tile[3]);
    cout << endl;
    print(tile[88]);
*/

/* if a side matches, it matches with one tile only */
/*    
    for (int i = 0; i < n; ++i)
    {
        cout << num_of_matches_upper_side(i) << " ";
        rotate(tile[i]);
        cout << num}_of_matches_upper_side(i) << " ";
        rotate(tile[i]);
        cout << num_of_matches_upper_side(i) << " ";
        rotate(tile[i]);
        cout << num_of_matches_upper_side(i) << endl;
    }
*/
    f.close();
    g.close();
    return 0;
}