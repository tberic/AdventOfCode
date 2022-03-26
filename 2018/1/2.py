f = open('input.txt', 'r')

lines = [int(line.strip()) for line in f]

used = set([0])

s = 0
done = False
while not done:
    for x in lines:
        s += x
        if s in used:
            print(s)
            done = True
            break
        used.add(s)

f.close()