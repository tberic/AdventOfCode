#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>

using namespace std;

map<string, string> passport;

void print()
{
    cout << "[" << passport.size() << "]  ";

        cout << "byr: " << passport["byr"] << "\t";
        cout << "cid: " << passport["cid"] << ((passport["cid"].size() <= 2) ? "\t\t" : "\t");
        cout << "ecl: " << passport["ecl"] << "\t";
        cout << "eyr: " << passport["eyr"] << "\t";
        cout << "hcl: " << passport["hcl"] << "\t";
        cout << "hgt: " << passport["hgt"] << "\t";
        cout << "iyr: " << passport["iyr"] << "\t";
        cout << "pid: " << passport["pid"] << "\t";

/*
    for (map<string, string>::iterator it = passport.begin(); it != passport.end(); it++)    
        cout << it->first << ":" << it->second << "\t";    
*/

    cout << endl;
}

void reset()
{
    passport.clear();
}

int validate()
{
    if ( (passport.size() == 7) && (passport.count("cid") > 0) )
    {
        //cout << "[too few data] ";
        //print();
        return 0;
    }
    if (passport.size() < 7)
    {
        //cout << "[too few data] ";
        //print();
        return 0;
    }
// from this point all (necessary) fields are present
    
    if (passport["byr"] < "1920" || passport["byr"] > "2002")
    {
        //cout << "[byr invalid] ";
        //print();
        return 0;
    }
    if (passport["iyr"] < "2010" || passport["iyr"] > "2020")
    {
        //cout << "[iyr invalid] ";
        //print();
        return 0;
    }
    if (passport["eyr"] < "2020" || passport["eyr"] > "2030")
    {
        //cout << "[eyr invalid] ";
        //print();
        return 0;
    }

    string height = passport["hgt"].substr(0, passport["hgt"].size()-2);
    string units = passport["hgt"].substr(passport["hgt"].size()-2);
    
    if ( (units != "cm") && (units != "in") )
    {
        //cout << "[hgt invalid] ";
        //print();
        return 0;
    }
    if (units == "cm" && (height < "150" || height > "193"))
    {
        //cout << "[hgt invalid] ";
        //print();
        return 0;
    }
    if (units == "in" && (height < "59" || height > "76"))
    {
        //cout << "[hgt invalid] ";
        //print();
        return 0;
    }

    if (passport["hcl"].at(0) != '#' || passport["hcl"].size() != 7)
    {
        //cout << "[hcl invalid] ";
        //print();
        return 0;
    }
    for (int i = 1; i <= 6; i++)    
        if ( ((passport["hcl"].at(i) < '0') || (passport["hcl"].at(i) > '9')) && ((passport["hcl"].at(i) < 'a') || (passport["hcl"].at(i) > 'f')) )
    {
        //cout << "[hcl invalid] ";
        //print();
        return 0;
    }

    if (passport["ecl"] != "amb" && passport["ecl"] != "blu" && passport["ecl"] != "brn" && passport["ecl"] != "gry" && passport["ecl"] != "grn" && passport["ecl"] != "hzl" && passport["ecl"] != "oth")
    {
        //cout << "[ecl invalid] ";
        //print();
        return 0;
    }

    if ( passport["pid"].size() != 9 )
        return 0;
    
    if ( passport["pid"] < "000000000" || passport["pid"] > "999999999" )
    {
        //cout << "[pid invalid] ";
        //print();
        return 0;
    }

    print();
    return 1;
}

int main()
{
    ifstream f;
    f.open("input.txt");
    string word, line, key, value;
    int n = 0;

    reset();
    while (getline(f, line))
    {
        if (line.empty())
        {
            n += validate();
            // print();
            reset();
        }
        else
        {
            istringstream iss(line);
            while (iss >> word)
            {
                key = word.substr(0, word.find(":"));
                value = word.substr(word.find(":")+1);
                passport[key] = value;
            }
        }
    }
    n += validate();

    cout << n << endl;
        
    f.close();
    return 0;
}