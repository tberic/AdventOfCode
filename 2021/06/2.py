f = open('input.txt', 'r')
line = f.readline()

timer = [0 for i in range(9)]

for num in line.split(','):
    timer[int(num)] += 1
    
for day in range(256):
    zeros = timer[0]
    for i in range(1, 9):
        timer[i-1] = timer[i]
    timer[6] += zeros
    timer[8] = zeros

count = 0
for i in range(9):
    count += timer[i]
print(count)

f.close()
