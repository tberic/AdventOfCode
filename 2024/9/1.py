def find(id, pos):
    while disk[pos] != id:
        pos -= 1
    while disk[pos] == id:
        pos -= 1
    return pos+1

def nextZero(pos):
    while disk[pos] != 0:
        pos += 1
    return pos

f = open('input.txt')

text = f.readline().strip()
disk = [0 for i in range(len(text)*9)]

pos = 0
id = 1
lastBlock = 0
lastId = 0
for index, ch in enumerate(text):
    digit = int(ch)
    if index%2 == 0:
        lastBlock = pos
        lastId = id
        for i in range(digit):
            disk[pos] = id
            pos += 1
        id += 1        
    else:
        pos += digit


startPos = nextZero(0)
id = lastId
endPos = find(id, lastBlock)
while startPos < endPos:
    while disk[endPos] != 0 and disk[startPos] == 0:
        disk[endPos] = 0
        disk[startPos] = id
        endPos += 1
        startPos = nextZero(startPos)
    
    id -= 1
    endPos = find(id, lastBlock)
    startPos = nextZero(startPos)

pos = 0
checksum = 0
while disk[pos] != 0:
    checksum += pos * (disk[pos]-1)
    pos += 1

print(checksum)