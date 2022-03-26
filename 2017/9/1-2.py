def score(i, j, x):
    global line

#    print(i, j, x, line[i:j])

    if i > j:
        return 0

    if i == j:
        return x

    s = x
    while i < j:

        while line[i] != '{':
            i += 1
        
        brackets = 1
        b = i + 1
        while brackets:
            if line[b] == '{':
                brackets += 1
            elif line[b] == '}':
                brackets -= 1
            b += 1

        s += score(i+1, b-1, x+1)

        i = b

    return s


f = open('input-reduced.txt', 'r')
line = f.readline().strip()
f.close()

#line = "{{{},{},{{}}}}"

#print(score(0, len(line), 0))

s = 0
depth = 0
i = 0
while i < len(line):

    if line[i] == '{':
        depth += 1
    elif line[i] == '}':
        s += depth
        depth -= 1

    i += 1

print(s)