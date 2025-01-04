def consistent(s, groups):
    i = 0
    pos = 0
    size = 0
    s += '.'
    while i < len(s):
        if s[i] == '#':
            size += 1
        if s[i] == '.' and size > 0:
            if pos >= len(groups):
                return 0
            if size != groups[pos]:
                return 0
            size = 0
            pos += 1

        i += 1
    
    if pos == len(groups):
        return 1
    return 0

def ways(s, groups):
    if '?' not in s:
        return consistent(s, groups)
    
    s1 = s.replace('?', '.', 1)
    s2 = s.replace('?', '#', 1)
    return ways(s1, groups) + ways(s2, groups)
    

f = open('input.txt', 'r')

sum = 0
for line in f:
    springs, groupsIn = line.strip().split(' ')
    groups = [int(x) for x in groupsIn.split(',')]
    sum += ways(springs, groups)

print(sum)