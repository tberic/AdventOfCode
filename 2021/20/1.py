def pixel(x, y):
    global image
    s = str(image[x-1][y-1])+str(image[x-1][y])+str(image[x-1][y+1])+\
        str(image[x][y-1])+str(image[x][y])+str(image[x][y+1])+\
            str(image[x+1][y-1])+str(image[x+1][y])+str(image[x+1][y+1])    
    n = int(s, 2)    
    return n


def convert(c):
    if c == '.':
        return 0
    return 1

f = open('input.txt', 'r')

lines = [line.strip() for line in f]
algo = lines[0]
grid = lines[2:]
n = len(grid)
steps = 50
padding = steps*2
N = n+2*padding

image = [[0 for i in range(N)] for j in range(N)]
for i in range(n):
    for j in range(n):
        image[i+padding][j+padding] = convert(grid[i][j])
#print(image)

for _ in range(steps):
    new_image = [[0 for i in range(N)] for j in range(N)]
    for i in range(1,N-1):
        for j in range(1, N-1):
            new_image[i][j] = convert(algo[pixel(i,j)])
            #print(algo[pixel(i,j)], end='')
        #print()
    #print()
    #print()
    image = new_image

count = 0
for i in range(-steps, n+steps):
    for j in range(-steps, n+steps):
        count += image[i+padding][j+padding]
print(count)

f.close()