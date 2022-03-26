def sumSafe(s):
    count = 0
    for c in s:
        if c == '.':
            count += 1
    return count


f = open('input.txt', 'r')
last = f.readline().strip()
f.close()

n = len(last)
last = '.' + last + '.'

count = sumSafe(last[1:-1])
m = 400000
for i in range(1, m):
    print(i)
    row = '.'
    for j in range(1, n+1):
        if ( last[j-1]  == '^' and last[j]  == '^' and last[j+1]  == '.') or \
            ( last[j-1]  == '.' and last[j]  == '^' and last[j+1]  == '^') or \
            ( last[j-1]  == '^' and last[j]  == '.' and last[j+1]  == '.') or \
            ( last[j-1]  == '.' and last[j]  == '.' and last[j+1]  == '^'):
            row += '^'
        else:
            row += '.'
    row += '.'
    count += sumSafe(row[1:-1])
    last = row[:]

print(count)