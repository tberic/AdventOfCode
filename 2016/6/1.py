from collections import Counter

f = open('input.txt', 'r')
col = [""] * 8
for line in f:
    for i in range(8):
        col[i] += line[i]
f.close()

for i in range(8):
    print(Counter(col[i]).most_common(1)[0][0], end='')