#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class BigInteger
{
private:
    string n;
public:
    BigInteger(string s = "") { n = s; }
    BigInteger(int x) { n = to_string(x); }
    
    char& operator[](int i)
    {
        return n[i];
    }
    
    friend BigInteger operator+(BigInteger a, BigInteger b)
    {
        BigInteger c;
        
        if (a.n.length() > b.n.length())
            b.n = string(a.n.length()-b.n.length(), '0') + b.n;
        else if (b.n.length() > a.n.length())
            a.n = string(b.n.length()-a.n.length(), '0') + a.n;
            
        int carry = 0;
        for (int i = a.n.length()-1; i >= 0; i--)
        {
            char dig = (a[i]-'0' + b[i]-'0' + carry) % 10 + '0';
            c.n = string(1, dig) + c.n;
            carry = (a[i]-'0' + b[i]-'0' + carry) / 10;
        }
        if (carry)
            c.n = to_string(carry) + c.n;
        
        return c;
    }

    // simpler version of multiply - the second argument is a char
    friend string operator*(BigInteger a, char b)
    {
        BigInteger c;
        int carry = 0;
        for (int i = a.n.length()-1; i >= 0; i--)
        {
            char dig = ((a[i]-'0')*(b-'0')+ carry) % 10 + '0';
            c.n = string(1, dig) + c.n;
            carry = ((a[i]-'0')*(b-'0')+ carry) / 10;
        }
        if (carry)
            c.n = to_string(carry) + c.n;
        
        return c.n;
    }
    
    friend BigInteger operator*(BigInteger a, BigInteger b)
    {
        BigInteger c(0);
        int zeros = 0;

        for (int i = b.n.length()-1; i >= 0; i--)
        {
            c = c + BigInteger( ( a*(char)b[i] )+ string(zeros, '0') );
            zeros++;
        }
        
        return c;
    }

    friend ostream& operator<<(ostream &out, const BigInteger &a)
    {
        out << a.n;
        return out;        
    }   
};


int main()
{
    ifstream f("input.txt");
    int x;
    char c;
    BigInteger timer[9];
    int initialTimer[9] = {0};
    
    while (f >> x >> c)
        initialTimer[x]++;
    f >> x;
    initialTimer[x]++;

    for (int i = 0; i <= 8; ++i)
        timer[i] = initialTimer[i];

    for (int day = 1; day <= 80; ++day)
    {
        // deal with zero times
        BigInteger zeros = timer[0];
        
        for (int i = 1; i <= 8; ++i)
            timer[i-1] = timer[i];
        
        timer[6] = timer[6] + zeros;
        timer[8] = zeros;
    }

    BigInteger count = 0;
    for (int i = 0; i <= 256; ++i)
        count = count + timer[i];
    cout << count << endl;

    f.close();
    return 0;
}