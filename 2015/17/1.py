def containers(pos, vol):
    global c, take, liters

    if vol < 0:
        return 0
    if pos == len(c):
        if vol == 0:
            return 1
        else:
            return 0

    return containers(pos+1, vol) + containers(pos+1, vol-c[pos])
    
liters = 150

f = open('input.txt', 'r')
c = []
for line in f:
    c.append(int(line))
f.close()

print(containers(0, liters))