f = open('input.txt', 'r')

for line in f:
    for x in line.split(','):
        print(int(x))


f.close()