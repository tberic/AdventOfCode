f = open('input.txt', 'r')

grid = [[9 for i in range(102)]]

for line in f:
        line = line[:-1]
        line = '9' + line + '9'
        a = [int(x) for x in line]
        grid.append(a)

a = [9 for i in range(102)]
grid.append(a)

sum = 0
for i in range(1, 101):
        for j in range(1, 101):
                if (grid[i][j] < grid[i-1][j] and grid[i][j] < grid[i+1][j] 
                and grid[i][j] < grid[i][j-1] and grid[i][j] < grid[i][j+1]):
                        sum += grid[i][j]+1
        
print(sum)

f.close()
