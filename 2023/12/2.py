import functools

def possibleGroup(s, n):
    if len(s) < n:
        return False
    groupPossible = all([ c == '#' or c == '?' for c in s[:n] ])
    if len(s) == n:
        return groupPossible
    return groupPossible and s[n] != '#'

@functools.lru_cache(maxsize=None)
def ways(s, groups):
    if len(s) == 0:
        return len(groups) == 0
    
    if s[0] == '.':
        return ways(s[1:], groups)

    if s[0] == '#':
        if len(groups) == 0:
            return 0
        if possibleGroup(s, groups[0]):
            return ways(s[groups[0]+1:], groups[1:])

    if s[0] == '?':
        return ways(s[1:], groups) + ways('#' + s[1:], groups)

    return 0

f = open('input.txt', 'r')

sumWays = 0
for lineNum, line in enumerate(f):
    springs, groupsIn = line.strip().split(' ')
    springs = (springs + '?') * 4 + springs
    springs += '.'

    groups = [int(x) for x in groupsIn.split(',')]
    groups = groups * 5

    groupsTarget = groups
    w = ways(springs, tuple(groups))
    print(lineNum, w)
    sumWays += w

print(sumWays)