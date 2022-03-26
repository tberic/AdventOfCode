def iscomposite(x):
    if x%2 == 0:
        return 1
    d = 3
    while d*d <= x:
        if x%d == 0:
            return 1
        d += 2
    return 0

count = 0
for x in range(109900, 126901, 17):
    count += iscomposite(x)
print(count)