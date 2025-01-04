import re

def abba(s):
    for i in range(len(s)-3):
        if s[i] != s[i+1] and s[i+2] == s[i+1] and s[i+3] == s[i]:
            return True
    return False

f = open('input.txt', 'r')

count = 0
for line in f:
    s = "]" + line.strip() + "["
    
    # outside brackets
    m = re.findall(r'\](.*?)\[', s)
    t = 0
    for x in m:
        if abba(x):
            t = 1
            break
    if t == 0:
        continue
    
    # inside brackets
    m = re.findall(r'\[(.*?)\]', s)
    t = 1
    for x in m:
        if abba(x):
            t = 0
            break
    if t == 0:
        continue

    count += 1
    #print(s)

print(count)

f.close()