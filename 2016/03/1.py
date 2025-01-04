f = open('input.txt', 'r')

count = 0
for line in f:
    x, y, z = list(map(int, line.split()))
    if x+y > z and x+z > y and y+z > x:
        count += 1

print(count)

f.close()