f = open('input-reduced.txt', 'r')
s = f.readline().strip()
f.close()

sum = 0
i = 0
while i < len(s):
    if s[i] not in '-0123456789':
        i += 1
        continue
    j = i
    while j < len(s) and s[j] in '-0123456789':
        j += 1    
    sum += int(s[i:j])
    i = j

print(sum)