#include <iostream>
#include <fstream>

using namespace std;

string s;

long long parse(int a, int b)
{
    int i = a;
    long long res;
    char op = ' ';

    while (i <= b)
    {
        if (s.at(i) >= '0' && s.at(i) <= '9')
        {
            if (op == '+')
                res += s.at(i)-'0';
            else if (op == '*')
                res *= s.at(i)-'0';
            else
                res = s.at(i)-'0';
        }
        if (s.at(i) == '+' || s.at(i) == '*')
        {
            op = s.at(i);
        }
        if (s.at(i) == '(')
        {
            //find corresponding closing bracket
            int j = i+1;
            int b = 0;
            while (s.at(j) != ')' || b > 0)
            {
                if (s.at(j) == '(') 
                    b++;
                if (s.at(j) == ')') 
                    b--;
                j++;
            }
            
            if (op == '+')
                res += parse(i+1, j-1);
            else if (op == '*')
                res *= parse(i+1, j-1);
            else 
                res = parse(i+1, j-1);
            i = j;
        }
        if (s.at(i) == ')')
        {
            
        }
        if (s.at(i) == ' ')
        {
            
        }

        i++;        
    }

//    cout << a << "-" << b << " ";
//    cout << res << endl;
    return res;
}

int main()
{
    ifstream f;
    f.open("input.txt");
    long long x, sum = 0;

    while (getline(f, s))
    {
        x = parse(0, s.size()-1);
        sum += x;
    }

    cout << endl << sum << endl;

    f.close();
    return 0;
}