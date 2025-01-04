#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <array>
using namespace std;

constexpr long MINX = 0;
constexpr long MAXX = 4000000;

struct Point
{
    Point(long xVal = 0, long yVal = 0) : x(xVal), y(yVal) {};
    long x, y;
};

struct HorizSegment
{
    HorizSegment(long x1 = 0, long x2 = 0, long yVal = 0) : 
        startX(x1), endX(x2), y(yVal) {};
    long startX, endX, y;
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
    long x1 = min(seg1.startX, seg2.startX);
    long x2 = max(seg1.endX, seg2.endX);
    return HorizSegment(x1, x2, seg1.y);
}

bool intersects(long x, long y, long r, long y0)
{
    return abs(y-y0) <= r;
}

HorizSegment findIntersect(long x, long y, long r, long y0)
{
    return HorizSegment( x - r + abs(y0 - y), x + r - abs(y0 - y), y0 );
}

int nPossiblePointsAtY(vector<Point> sensors, vector<Point> beacons, int y0)
{
    array<HorizSegment, 30> segs;
    HorizSegment nullSegment(0, 0, 0);

    for (int j = 0; j < sensors.size(); ++j)
    {
        long r = abs(sensors[j].x - beacons[j].x) + abs(sensors[j].y - beacons[j].y);
        
        if (intersects(sensors[j].x, sensors[j].y, r, y0))
        {
            HorizSegment seg = findIntersect(sensors[j].x, sensors[j].y, r, y0);
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
    }

    long length = 0;
    for (auto seg : segs)
        if (!isNullSeg(seg))
        {
            cout << seg.startX << " " << seg.endX << " " << seg.y << endl;
            length += min(seg.endX, MAXX) - max(seg.startX, MINX) + 1;
        }

    return length;
}

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    if (!fin || !fout)
    {
        return 1;
    }

    vector<Point> sensors, beacons;
    long sensorX, sensorY, beaconX, beaconY;
    string line;
    while (getline(fin, line))
    {
        stringstream in(line);
        in >> sensorX >> sensorY >> beaconX >> beaconY;
        sensors.push_back( Point(sensorX, sensorY) );
        beacons.push_back( Point(beaconX, beaconY) );
    }

    // int y0;
    // for(y0 = 0; y0 <= MAXX; ++y0)
    //     if (nPossiblePointsAtY(sensors, beacons, y0) < MAXX+1)
    //         break;
            // cout << y0 << endl;

    int y0 = 2601918;
    nPossiblePointsAtY(sensors, beacons, y0);

    for (int x0 = 0; x0 <= MAXX; ++x0)
    {
        bool found = false;
        for (int i = 0; i < sensors.size(); ++i)
            if (abs(sensors[i].x - x0) + abs(sensors[i].y - y0) <= 
                abs(sensors[i].x - beacons[i].x) + abs(sensors[i].y - beacons[i].y))
            {
                found = true;
                break;
            }
        if (!found)
        {
            long long res = MAXX*x0 + y0;
            cout << res << endl; // WRONG result, I multiplied it in wolframalpha
            cout << x0 << " " << y0 << endl;
        }
    }

    fin.close();
    fout.close();
    return 0;
}