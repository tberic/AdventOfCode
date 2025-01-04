#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <array>
using namespace std;

struct Point
{
    Point(int xVal = 0, int yVal = 0) : x(xVal), y(yVal) {};
    int x, y;
};

struct HorizSegment
{
    HorizSegment(int x1 = 0, int x2 = 0, int yVal = 0) : startX(x1), endX(x2), y(yVal) {};
    int startX, endX, y;
};

bool isNullSeg(HorizSegment seg)
{
    return seg.startX == 0 && seg.endX == 0 && seg.y == 0;
}

bool overlap(HorizSegment seg1, HorizSegment seg2)
{
    if (seg1.y != seg2.y)
        return false;

    return (seg2.startX <= seg1.endX && seg1.endX <= seg2.endX) ||
            (seg1.startX <= seg2.endX && seg2.endX <= seg1.endX);
}

HorizSegment segUnion(HorizSegment seg1, HorizSegment seg2)
{
    int x1 = min(seg1.startX, seg2.startX);
    int x2 = max(seg1.endX, seg2.endX);
    return HorizSegment(x1, x2, seg1.y);
}

bool intersects(int x, int y, int r, int y0)
{
    return abs(y-y0) <= r;
}

HorizSegment findIntersect(int x, int y, int r, int y0)
{
    return HorizSegment( x - r + abs(y0 - y), x + r - abs(y0 - y), y0 );
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout)
    {
        return 1;
    }

    int sensorX, sensorY, beaconX, beaconY;
    string line;
    int y0 = 2000000;
    array<HorizSegment, 100> segs;
    HorizSegment nullSegment(0, 0, 0);
    vector<Point> beacons;
    while (getline(fin, line))
    {
        stringstream in(line);
        in >> sensorX >> sensorY >> beaconX >> beaconY;
        int found = 0;
        for (int i = 0; i < beacons.size(); ++i)
            if (beacons[i].x == beaconX && beacons[i].y == beaconY)
                found = 1;
        if (!found)
            beacons.push_back( Point(beaconX, beaconY) );                

        int r = abs(sensorX - beaconX) + abs(sensorY - beaconY);
        
        if (intersects(sensorX, sensorY, r, y0))
        {
            HorizSegment seg = findIntersect(sensorX, sensorY, r, y0);
            for (int i = 0; i < segs.size(); ++i)
            {
                if (overlap(seg, segs[i]))
                {
                    seg = segUnion(seg, segs[i]);
                    segs[i] = nullSegment;
                }
            }
            
            for (int i = 0; i < segs.size(); ++i)
                if (isNullSeg(segs[i]))
                {
                    segs[i] = seg;
                    break;
                }
        }

        // cout << intersects(sensorX, sensorY, abs(sensorX - beaconX) + abs(sensorY - beaconY), y0) << endl;
    }

    int length = 0;
    for (auto seg : segs)
        if (!isNullSeg(seg))
            length += seg.endX - seg.startX + 1;
            // cout << seg.startX << " " << seg.endX << " " << seg.y << endl;

    int nBeacons = 0;
    for (int i = 0; i < beacons.size(); ++i)
        if (beacons[i].y == y0)
            nBeacons++;

    length -= nBeacons;

    cout << length << endl;

    fin.close();
    fout.close();
    return 0;
}