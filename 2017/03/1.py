n = 347991

i = 1
while (2*i+1)**2 < n:
    i += 1

m = n - (2*i-1)**2
print(i, 2*i-1, (2*i-1)**2, m)

x,y = (i-1, i-1)
y += 1
m -= 1
print((x, y), m)

x -= 2*i-1
m -= 2*i-1
print((x, y), m)

y -= m
m -= m
print((x, y), m)
print(abs(x)+abs(y))