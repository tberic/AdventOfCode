a = 618
b = 814
na = 16807
nb = 48271
m = 2147483647

count = 0
N = 40000000
for _ in range(N):
    a = (a*na) % m
    b = (b*nb) % m

    if bin(a).zfill(16)[-16:] == bin(b).zfill(16)[-16:]:
        count += 1

print(count)