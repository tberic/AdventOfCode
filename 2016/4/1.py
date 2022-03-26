from collections import Counter
import re

f = open('input.txt', 'r')
g = open('input2.txt', 'w')

sum = 0
for line in f:
    m = re.search(r'(.*)\-(\d+)\[(.*)\]', line)
    room, ID, checksum = m.groups()
    ID = int(ID)
    
    room = re.sub('-', '', room)
    hist = Counter(room).most_common()
    for i in range(len(hist)):
        for j in range(i+1, len(hist)):
            if hist[i][1] < hist[j][1]:
                t = hist[i]
                hist[i] = hist[j]
                hist[j] = t
            elif hist[i][1] == hist[j][1] and hist[i][0] > hist[j][0]:
                t = hist[i]
                hist[i] = hist[j]
                hist[j] = t
    t = hist[0][0] + hist[1][0] + hist[2][0] + hist[3][0] + hist[4][0]
    #print(t)
    if t == checksum:
        sum += ID
        print(room+'-'+str(ID), file=g)

print(sum)

f.close()
g.close()