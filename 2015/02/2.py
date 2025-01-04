f = open('input.txt', 'r')
total = 0
for line in f:
    a,b,c = list(map(int, line.split('x')))
    x = sorted([a, b, c])    
    total += a*b*c + 2*x[0] + 2*x[1]
f.close()

print(total)