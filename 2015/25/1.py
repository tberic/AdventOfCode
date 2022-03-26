x, y = (2947, 3029)

seed = 20151125
mult = 252533
mod = 33554393

n = seed
i, j = (1, 1)
while (i, j) != (x, y):
    if i == 1:
        i = j+1
        j = 1
    else:
        i -= 1
        j += 1
    n = (n*mult) % mod

print(n)