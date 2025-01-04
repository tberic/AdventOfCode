f = open('input.txt')

text = f.readline().strip()
zeros = []
blocks = []

pos = 0
id = 0
for index, ch in enumerate(text):
    length = int(ch)
    if index%2 == 0:
        blocks.append([pos, length])
        pos += length
        id += 1
    else:        
        if length > 0:
            zeros.append([pos, length])
        pos += length

while id > 0:
    id -= 1
    for i in range(len(zeros)):
        if zeros[i][0] < blocks[id][0] and zeros[i][1] >= blocks[id][1]:
            blocks[id][0] = zeros[i][0]
            zeros[i][0] += blocks[id][1]
            zeros[i][1] -= blocks[id][1]
            if zeros[i][1] == 0:
                zeros.pop(i)
            break

checksum = 0
for id, block in enumerate(blocks):
    for pos in range(block[1]):
        checksum += (block[0]+pos) * id
print(checksum)