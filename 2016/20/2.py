f = open('input-reduced.txt', 'r')
a = [ list(map(int, line.strip().split('-'))) for line in f ]
f.close()

count = 0
last = -1
for x in a:
    count += x[0]-last-1
    last = x[1]
count += 4294967295-last
print(count)