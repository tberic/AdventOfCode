import hashlib
from collections import deque

start = "qzthpkfp"

Q = deque()
Q.append( (0, 0, start, "") )

# longest path
maxLength = 0
while Q:
    x, y, s, path = Q.popleft()

    if x == 3 and y == 3:
        #print('Found: ' + str(len(path)))
        if len(path) > maxLength:
            maxLength = len(path)
        continue

    #print(x, y, s, path, end=':::')

    next = hashlib.md5(s.encode()).hexdigest()
    #print(next[:4])
    
    if y > 0 and next[0] in 'bcdef':
        Q.append( (x, y-1, s+'U', path+'U') )
    if y < 3 and next[1] in 'bcdef':
        Q.append( (x, y+1, s+'D', path+'D') )
    if x > 0 and next[2] in 'bcdef':
        Q.append( (x-1, y, s+'L', path+'L') )
    if x < 3 and next[3] in 'bcdef':
        Q.append( (x+1, y, s+'R', path+'R') )

print(maxLength)