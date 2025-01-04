f = open('input.txt')

stones = list(map(int, f.readline().strip().split(' ')))

STEPS = 25

for step in range(STEPS):
    stones2 = []
    for i, stone in enumerate(stones):
        if stone == 0:
            stones2.append(1)
        elif len(str(stone)) % 2 == 0:
            txt = str(stone)
            left = int(txt[:len(txt)//2])
            right = int(txt[len(txt)//2:])
            stones2.append(left)
            stones2.append(right)
        else:
            stones2.append( stone * 2024 )
    
    stones = stones2

print(len(stones))