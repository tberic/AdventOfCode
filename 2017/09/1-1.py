f = open('input.txt', 'r')
line = f.readline().strip()
f.close()

g = open('input-reduced.txt', 'w')

i = 0
comment = 0
garbage = 0
while i < len(line):
    if line[i] == '<' and not comment:
        comment = 1
    elif line[i] == '>' and comment:
        comment = 0
    elif line[i] == '!':
        i += 1
    elif comment:
        garbage += 1
    else:
        print(line[i], file=g, end='') 

    i += 1

g.close()

print(garbage)