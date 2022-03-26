f = open('scanners.txt', 'r')

scanner = []
for line in f:
    i, nums = line.split(':')
    x,y,z,a = list(map(int, nums.split()))
    scanner.append((x,y,z))

maxDist = 0
for x,y,z in scanner:
    for a,b,c in scanner:
        if abs(x-a)+abs(y-b)+abs(z-c) > maxDist:
            maxDist = abs(x-a)+abs(y-b)+abs(z-c)

print(maxDist)
