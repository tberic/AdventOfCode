from copy import deepcopy
from functools import lru_cache 

@lru_cache(maxsize=1000000000)
def next_step(stone):
    if stone == 0:
        return [1]
    
    if len(str(stone)) % 2 == 0:
        txt = str(stone)
        left = int(txt[:len(txt)//2])
        right = int(txt[len(txt)//2:])
        return [left, right]
    else:
        return [stone * 2024]

STEPS = 75

f = open('input.txt')

stones = list(map(int, f.readline().strip().split(' ')))

grouped = { stone: stones.count(stone) for stone in stones }

for step in range(STEPS):
    grouped_next = {}
    for stone, cnt in grouped.items():
        res = next_step(stone)

        for x in res:
            if x not in grouped_next:
                grouped_next[x] = cnt
            else:
                grouped_next[x] += cnt

    grouped = grouped_next

total = 0
for _, cnt in grouped.items():
    total += cnt
print(total)