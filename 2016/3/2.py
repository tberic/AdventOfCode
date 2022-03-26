f = open('input.txt', 'r')
lines = [ list(map(int, line.strip().split())) for line in f]
f.close()

count = 0
for i in range(len(lines)//3):
    for j in range(3):
        x, y, z = lines[3*i][j], lines[3*i+1][j], lines[3*i+2][j]
        if x+y > z and x+z > y and y+z > x:
            count += 1

print(count)