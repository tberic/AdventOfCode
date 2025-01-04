def decompress(s):
    if '(' not in s:
        return len(s)
    
    i = 0
    l = 0
    while i < len(s):
        if s[i] != '(':
            l += 1
            i += 1
        else:
            j = i
            while s[j] != ')':
                j += 1
            m, n = list(map(int, s[i+1:j].split('x')))
            l += n*decompress(s[j+1:j+1+m])
            i = j+m+1
    return l
       

f = open('input.txt', 'r')
s = f.readline().strip()
f.close()

print(decompress(s))