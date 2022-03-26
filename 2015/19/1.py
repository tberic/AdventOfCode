f = open('input.txt', 'r')

lines = [line.strip() for line in f]
s = lines[-1]
replace = {}
for x in lines[:-2]:
    a, b = x.split(' => ')
    if a not in replace:
        replace[a] = [b]
    else:
        replace[a].append(b)
f.close()

molecules = set()

for i in range(len(s)):
    if s[i] in replace:
        for x in replace[s[i]]:
            molecules.add( s[:i] + x + s[i+1:] )
    if i+1 < len(s) and s[i:i+2] in replace:
        for x in replace[s[i:i+2]]:
            molecules.add( s[:i] + x + s[i+2:] )

print(len(molecules))