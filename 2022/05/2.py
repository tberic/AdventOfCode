from collections import deque
nHeaps = 9
fin = open('input.txt', 'r')

q = [deque() for i in range(nHeaps)]

for line in fin:
    if line.strip() == "":
        break
    for k in range(nHeaps):
        if line[4*k+1] != ' ' and (line[4*k+1] not in "123456789"):
            q[k].append(line[4*k+1])
            
# print(q)

for line in fin:
    parseStr = line.strip().split(' ')
    qty = int(parseStr[1])
    a = int(parseStr[3])
    b = int(parseStr[5])

    tmpStack = []
    for i in range(qty):
        tmpStack.append(q[a-1].popleft())

    while tmpStack:
        q[b-1].appendleft(tmpStack.pop())

    # print(q)

for k in  range(nHeaps):
    print(q[k][0], end='')
