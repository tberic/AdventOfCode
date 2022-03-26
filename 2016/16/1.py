def fill(n, a):
    while len(a) < n:
        a = step(a)
    return a[:n]

def step(a):
    l = list(a)
    l.reverse()
    for i in range(len(l)):
        if l[i] == '0':
            l[i] = '1'
        elif l[i] == '1':
            l[i] = '0'
    b = "".join(l)
    return a+'0'+b

# len(s) will be even
def checksum(s):
    t = ""
    while len(t)%2 == 0:
        t = ""
        for i in range(0, len(s), 2):
            if s[i] == s[i+1]:
                t += '1'
            else:
                t += '0'
        s = t
    
    return t
   

start = "11100010111110100"
#length = 272
length = 35651584

#print(step('111100001010'))
#print(checksum('110010110100'))
print(checksum(fill(length, start)))