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

buyers = []

for line in f:
    seed = int(line.strip())
    # print(seed)

    buyers.append([seed % 10])

    for _ in range(2000):
        seed = next(seed)    
        buyers[-1].append(seed % 10)

best = 0
for a in range(-9, 10):
    for b in range(-9, 10):
        for c in range(-9, 10):
            for d in range(-9, 10):
                bananas = 0
                for buyer in buyers:
                    for i in range(1, len(buyer) - 4):
                        if buyer[i]-buyer[i-1] == a and buyer[i+1]-buyer[i] == b and buyer[i+2]-buyer[i+1] == c and buyer[i+3]-buyer[i+2] == d:
                            bananas += buyer[i+3]
                            break
                if bananas > best:
                    best = bananas

print(best)