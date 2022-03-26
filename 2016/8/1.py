def ispis(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end='')
        print()
        
f = open('input.txt', 'r')

m = 6
n = 50
display = [['.' for j in range(n)] for i in range(m)]

for line in f:
    words = line.strip().split()
    if words[0] == "rect":
        b, a = list(map(int, words[1].split('x')))
        for i in range(a):
            for j in range(b):
                display[i][j] = '#'

    elif words[0] == "rotate" and words[1] == "row":
        a = int(words[2][2:])
        b = int(words[4])
        row = ['.' for i in range(n)]
        for i in range(n):
            row[(i+b)%n] = display[a][i]
        for i in range(n):
            display[a][i] = row[i]
                
    elif words[0] == "rotate" and words[1] == "column":
        a = int(words[2][2:])
        b = int(words[4])
        col = ['.' for i in range(m)]
        for i in range(m):
            col[(i+b)%m] = display[i][a]
        for i in range(m):
            display[i][a] = col[i]

count = 0
for i in range(m):
    for j in range(n):
        count += display[i][j]=='#'

print(count)
ispis(display)

f.close()