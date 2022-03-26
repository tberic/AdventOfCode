x = 369

N = 50000000
pos = 0
afterZero = 0
for i in range(1, N+1):    
    pos = (pos + x) % i
    if pos == 0:
        afterZero = i
    pos += 1

print(afterZero)