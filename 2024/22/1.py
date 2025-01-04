def mix(x, y):
    return x ^ y

def prune(x):
    return x % 16777216

def next(num):
    a = prune(mix(num * 64, num))
    b = prune(mix(a // 32, a))
    c = prune(mix(b * 2048, b))
    return c

f = open('input.txt')

total = 0
for line in f:
    seed = int(line.strip())
    print(seed)

    for _ in range(2000):
        seed = next(seed)
    total += seed

print(total)