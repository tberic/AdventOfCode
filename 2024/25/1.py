def fit(key, lock):
    for i in range(N):
        if key[i] + lock[i] > M:
            return False
    return True


def convert_to_heights(keylock):
    heights = [0 for j in range(N)]
    for j in range(N):
        for i in range(M):
            heights[j] += keylock[i][j] == '#'
    return heights

f = open('input.txt')

M = 7
N = 5

lines = [line.strip() for line in f]

locks = []
keys = []

# lock = (lines[0][0] == '.')
keylock = []
i = 0
while i < len(lines):
    if lines[i] == '':
        heights = convert_to_heights(keylock)
        i += 1
        if keylock[0][0] == '.':
            locks.append(heights)
        else:
            keys.append(heights)
        
        # print(keylock)
        keylock = []
        continue

    keylock.append(lines[i])
    i += 1

heights = convert_to_heights(keylock)
if keylock[0][0] == '.':
    locks.append(heights)
else:
    keys.append(heights)

# print(len(locks))
# print(len(keys))

total = 0
for i in range(len(keys)):
    for j in range(len(locks)):
        if fit(keys[i], locks[j]):
            total += 1
print(total)