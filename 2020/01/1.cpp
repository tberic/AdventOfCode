#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream f, g;
	f.open("input.txt");
	int x, y;

	while (!f.eof())
	{
		f >> x;

		g.open("input.txt");
		while (!g.eof())
		{
			g >> y;
			if (x + y == 2020) 
			{
				cout << x*y << endl;
				break;
			}
		}
		g.close();
	}

	f.close();
	g.close();
	return 0;
}