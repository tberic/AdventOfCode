f = open('output.txt', 'r')

beacons = set()

for line in f:
    x,y,z = list(map(int, line[1:-2].split(',')))
    beacons.add((x,y,z))

print(len(beacons))

# for x in sorted(beacons):
#     print(str(x)[1:-1])

f.close()