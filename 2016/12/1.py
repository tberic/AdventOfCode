f = open('input.txt', 'r')
lines = [line.strip() for line in f]
f.close()

register = { "a": 0, "b": 0, "c": 1, "d": 0 }

i = 0
while i < len(lines):
    words = lines[i].split()
    if words[0] == "cpy":
        x = words[1]
        y = words[2]
        if x[0] in '0123456789':
            register[y] = int(x)
        else:
            register[y] = register[x]
    if words[0] == "inc":
        register[ words[1] ] += 1
    if words[0] == "dec":
        register[ words[1] ] -= 1
    if words[0] == "jnz":
        if words[1][0] in '0123456789':
            x = int(words[1])
        else:
            x = register[ words[1] ]
        y = int(words[2])
        if x:
            i += y
            continue
    i += 1

print(register["a"])