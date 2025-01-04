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

indexed_bananas = {}
for index, buyer in enumerate(buyers):
    for i in range(1, len(buyer) - 3):
        a = buyer[i]-buyer[i-1]
        b = buyer[i+1]-buyer[i]
        c = buyer[i+2]-buyer[i+1]
        d = buyer[i+3]-buyer[i+2]
        
        if (a, b, c, d, index) not in indexed_bananas:
            indexed_bananas[(a, b, c, d, index)] = buyer[i+3]

# print(bananas)
bananas = {}
for key, value in indexed_bananas.items():
    a, b, c, d, index = key
    if (a, b, c, d) in bananas:
        bananas[(a, b, c, d)] += value
    else:
        bananas[(a, b, c, d)] = value

max = 0
for key, value in bananas.items():
    if value > max:
        max = value
print(max)