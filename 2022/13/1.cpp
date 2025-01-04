#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

bool isList(string &s)
{
    return (s[0] == '[');
}

vector<string> parse(string s)
{
    vector<string> result;
    int i = 0, last = 0;

    if (s == string("[]"))
        return result;

    s = s.substr(1, s.size()-2);
    s += ',';
    int brackets = 0;
    while (i < s.size())
    {
        if (s[i] == '[')
            brackets++;
        if (s[i] == ']')
            brackets--;
        if (s[i] == ',' && !brackets)
        {
            result.push_back(s.substr(last, i-last));
            last = i+1;
        }
        
        i++;
    }
    
    return result;
}

int compare(string lhs, string rhs)
{
    // cout << lhs << ":" << rhs << endl;
    if (lhs == "")
        return -1;
    if (rhs == "")
        return +1;

    int x, y;
    if (!isList(lhs) && !isList(rhs))
    {
        stringstream in1(lhs);
        stringstream in2(rhs);
        in1 >> x;
        in2 >> y;

        return (x-y);
    }

    if (!isList(lhs))
        return compare("["+lhs+"]", rhs);

    if (!isList(rhs))
        return compare(lhs, "["+rhs+"]");

    vector<string> lhsEl = parse(lhs);
    vector<string> rhsEl = parse(rhs);

    int i = 0;
    while (i < lhsEl.size() && i < rhsEl.size())
    {
        int result = compare(lhsEl[i], rhsEl[i]);
        if (result < 0)
            return -1;
        if (result > 0)
            return +1;
        
        ++i;
    }

    return (lhsEl.size() - rhsEl.size());
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout)
    {
        return 1;
    }

    string line1, line2;
    int index = 1, sum = 0;
    while (getline(fin, line1) && getline(fin, line2))
    {
        // cout << line1 << ":" << line2 << endl;
        int res = compare(line1, line2);
        if (res < 0)
        {
            cout << index << endl;
            sum += index;        
        }
        
        getline(fin, line1);
        index++;
    }

    cout << sum << endl;

    // vector<string> res = parse("[[1],[2,3,4]]");
    // for (auto s : res)
    //     cout << s << " ";
    // cout << endl;

    fin.close();
    fout.close();
    return 0;
}