from aoc import *
import re, z3

f = open('input.txt', 'r')

hail = []

for line in f:
    posString, velString = line.strip().split(' @ ')
    px, py, pz = [int(i) for i in posString.split(',')]
    vx, vy, vz = [int(i) for i in velString.split(',')]

    hail.append([px, py, pz, vx, vy, vz])

pxi, pyi, pzi, vxi, vyi, vzi = z3.Ints( "pxi pyi pzi vxi vyi vzi" )
ts = [ z3.Int( "t" + str(i) ) for i in range( len(hail) ) ]

s = z3.Solver()
for i, ( px, py, pz, vx, vy, vz ) in enumerate(hail):
    s.add( px + vx * ts[ i ] == pxi + vxi * ts[ i ] )
    s.add( py + vy * ts[ i ] == pyi + vyi * ts[ i ] )
    s.add( pz + vz * ts[ i ] == pzi + vzi * ts[ i ] )
s.check()
print( s.model().evaluate( pxi + pyi + pzi ) )
