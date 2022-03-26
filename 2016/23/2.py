f = open('input-modified.txt', 'r')
lines = [line.strip() for line in f]
f.close()

register = { "a": 479001600, "b": 0, "c": 0, "d": 0 }

i = 0
while i < len(lines):
    #print(i+1, lines[i], register)

    words = lines[i].split()
    x = words[1]
    if len(words) >= 3:
        y = words[2]

    if words[0][0] == '#':
        i += 1
        continue
    if words[0] == "cpy":
        if y[0] in '-0123456789':
            i += 1
            continue
        if x[0] in '-0123456789':
            register[y] = int(x)
        else:
            register[y] = register[x]
    elif words[0] == "inc":
        if x[0] in '-0123456789':
            i += 1
            continue
        register[ x ] += 1
    elif words[0] == "dec":
        if x[0] in '-0123456789':
            i += 1
            continue
        register[ x ] -= 1
    elif words[0] == "jnz":
        if x[0] in '-0123456789':
            x = int(x)
        else:
            x = register[x]
        if y[0] in '-0123456789':
            y = int(y)
        else:
            y = register[y]
        
        if x:
            i += y
            continue
    elif words[0] == "tgl":
        if x[0] in '-0123456789':
            x = int(x)
        else:
            x = register[x]
        if 0 <= i + x < len(lines):
            w = lines[i+x].split()
            if w[0] == "dec" or w[0] == "tgl":
                w[0] = "inc"
            elif w[0] == "inc":
                w[0] = "dec"
            elif w[0] == "jnz":
                w[0] = "cpy"
            elif w[0] == "cpy":
                w[0] = "jnz"
            lines[i+x] = " ".join(w)

    i += 1

print(register["a"])
