def different(a, b, c, d):
    l = [a, b, c, d]
    l.sort()
    if l[0] == l[1] or l[1] == l[2] or l[2] == l[3]:
        return False
    return True

fin = open('input.txt', 'r')

for line in fin:
    for j in range(3, len(line)):
        if different(line[j-3], line[j-2], line[j-1], line[j]):
            print(j+1)
            break
