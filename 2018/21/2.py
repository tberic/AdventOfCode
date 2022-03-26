seen = set()

a = 1
f = 0
while f != a:
    e = f | 65536
    f = 13284195
    while True: 
        d = e & 255
        f += d
        f &= 16777215
        f *= 65899
        f &= 16777215
        if e < 256:
            break

        e //= 256
		
    if f in seen:
        print('over')
        break
    seen.add(f)
    print(f)