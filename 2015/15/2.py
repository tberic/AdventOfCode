import re

def check(x):
    if x < 0:
        return 0
    return x

name = {}
n = 4
cap = [0 for i in range(n)]
dur = [0 for i in range(n)]
fla = [0 for i in range(n)]
tex = [0 for i in range(n)]
cal = [0 for i in range(n)]

f = open('input.txt', 'r')
n = 0
for line in f:
    m = re.search(r'(.+): capacity (\-?\d+), durability (\-?\d+), flavor (\-?\d+), texture (\-?\d+), calories (\-?\d+)', line)
    s, *l = m.groups()
    cap[n], dur[n], fla[n], tex[n], cal[n] = list(map(int, l))
    if s not in name:
        name[s] = n
        n += 1
f.close()

maxTotal = 0
for i1 in range(101):
    for i2 in range(101-i1):
        for i3 in range(101-i1-i2):
            i4 = 100-i1-i2-i3
            if cal[0]*i1 + cal[1]*i2 + cal[2]*i3 + cal[3]*i4 == 500:
                prodsum = check(cap[0]*i1 + cap[1]*i2 + cap[2]*i3 + cap[3]*i4) * \
                    check(dur[0]*i1 + dur[1]*i2 + dur[2]*i3 + dur[3]*i4) * \
                    check(fla[0]*i1 + fla[1]*i2 + fla[2]*i3 + fla[3]*i4) * \
                    check(tex[0]*i1 + tex[1]*i2 + tex[2]*i3 + tex[3]*i4)
                if prodsum > maxTotal:
                    maxTotal = prodsum

print(maxTotal)