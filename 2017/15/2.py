a = 618
b = 814
na = 16807
nb = 48271
m = 2147483647

count = 0
N = 5000000
for i in range(N):
    print(i)
    
    a = (a*na) % m
    while a % 4 != 0:
        a = (a*na) % m
    b = (b*nb) % m
    while b % 8 != 0:
        b = (b*nb) % m

    if bin(a).zfill(16)[-16:] == bin(b).zfill(16)[-16:]:
        count += 1

print(count)