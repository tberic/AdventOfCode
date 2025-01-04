def diff(s, t):
    count = 0
    pos = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
            pos = i
    return count, pos

f = open('input.txt', 'r')
lines = [line.strip() for line in f]
f.close()

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        cnt, pos = diff(lines[i], lines[j])
        if cnt == 1:
            print(lines[i][:pos] + lines[i][pos+1:])
            print(lines[j][:pos] + lines[j][pos+1:])
            break
