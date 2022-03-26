import hashlib
import re
from collections import deque

def hashStretch(s):
    for _ in range(2017):
        s = hashlib.md5(s.encode()).hexdigest()
    return s

salt = "jlmsuwbz"
#salt = "abc"

hash = deque()
for i in range(1001):
    hash.append( hashStretch(salt+str(i)) )

count = 0
i = 0
while True:
    s = hash.popleft()
    m = re.search(r'(.)\1\1', s)
    if m:
        t = 0
        c = m.groups()[0]
        for x in hash:
            if c*5 in x:
                t = 1
                break
        if t:
            count += 1
            if count == 64:
                print(i)
                break

    i += 1
    hash.append( hashStretch(salt+str(i+1000)) )