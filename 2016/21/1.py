def move(s, x, y):
    t = s[:x] + s[x+1:]
    return t[:y] + s[x] + t[y:]

def reverse(s, x, y):
    return s[:x] + ''.join(reversed(s[x:y+1])) + s[y+1:]

def swapPos(s, x, y):
    i = min(x, y)
    j = max(x, y)
    #print(' '*10, end='')
    #print(i, j)
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

def swapLetter(s, a, b):
    t = list(s)
    for i in range(len(s)):
        if t[i] == a:
            t[i] = b
        elif t[i] == b:
            t[i] = a
    return "".join(t)

def rotate(s, n=1):
    t = ""
    n = n % len(s)
    for i in range(len(s)):
        t += s[ (i-n)%len(s) ]
    return t

def rotatePos(s, c):
    n = s.find(c)
    if n >= 4:
        n += 1
    return rotate(s, n+1)

f = open('input.txt', 'r')

s = "abcdefgh"

i = 0
for line in f:
    i += 1
    words = line.strip().split()
    if words[0] == "swap" and words[1] == "position":
        x = int(words[2])
        y = int(words[5])
        s = swapPos(s, x, y)
    elif words[0] == "swap" and words[1] == "letter":
        a = words[2]
        b = words[5]
        s = swapLetter(s, a, b)
    elif words[0] == "rotate" and (words[1] == "left" or words[1] == "right"):
        x = int(words[2])
        if words[1] == "left":
            x = -x
        s = rotate(s, x)
    elif words[0] == "rotate" and words[1] == "based":
        c = words[6]        
        s = rotatePos(s, c)
    elif words[0] == "reverse":
        x = int(words[2])
        y = int(words[4])
        s = reverse(s, x, y)
    elif words[0] == "move":
        x = int(words[2])
        y = int(words[5])
        s = move(s, x, y)
    #print(i, s)

print(s)

f.close()