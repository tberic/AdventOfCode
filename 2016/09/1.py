f = open('input.txt', 'r')
s = f.readline().strip()
f.close()

i = 0
decompress = ""
while i < len(s):
    if s[i] != '(':
        decompress += s[i]
        i += 1
    else:
        j = i
        while s[j] != ')':
            j += 1        
        m, n = list(map(int, s[i+1:j].split('x')))
        for _ in range(n):
            decompress += s[j+1:j+1+m]
        i = j+m+1

print(len(decompress))