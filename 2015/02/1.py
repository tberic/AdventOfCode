f = open('input.txt', 'r')
total = 0
for line in f:
    a,b,c = list(map(int, line.split('x')))
    x = sorted([a, b, c])
    print(x)
    total += 2*(a*b + a*c + b*c) + x[0]*x[1]
f.close()

print(total)