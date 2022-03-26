def run():
    global lines, register, target

    i = 0
    cnt = 0
    next = 0
    while i < len(lines):
        #print(i+1, lines[i], end = ' ')
        #input()

        words = lines[i].split()
        x = words[1]
        if len(words) >= 3:
            y = words[2]

        if words[0][0] == '#': #ignore commented lines
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
        elif words[0] == "out":
            #print(register[words[1]])
            x = register[words[1]]
            if x != next:
                return False
            cnt += 1
            if cnt >= target:
                return True
            next = 1-next

        i += 1


f = open('input.txt', 'r')
lines = [line.strip() for line in f]
f.close()

target = 100

a = 0
while True:
    print(a)
    register = { "a": a, "b": 0, "c": 0, "d": 0 }
    if run():
        break
    a += 1

print(a)

#register = { "a": 192, "b": 0, "c": 0, "d": 0 }
#run()