f = open('input.txt', 'r')
line = f.readline()
f.close()

floor = 0
for c in line:
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1

print(floor)