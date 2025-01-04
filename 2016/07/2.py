import re

def aba(s, pos=0):
    for i in range(pos, len(s)-2):
        if s[i] != s[i+1] and s[i+2] == s[i]:
            return (s[i+1]+s[i]+s[i+1], i)
    return ("", 0)

f = open('input.txt', 'r')

count = 0
for line in f:
    s = "]" + line.strip() + "["
    
    # outside brackets
    m1 = re.findall(r'\](.*?)\[', s)
    # inside brackets
    m2 = re.findall(r'\[(.*?)\]', s)

    found = 0
    for x in m1:
        t, pos = aba(x)
        while t != "" and not found:
            for y in m2:
                if t in y:
                    found = 1
                    break
            t, pos = aba(x, pos+1)

    if not found:
        continue

    count += 1

print(count)

f.close()