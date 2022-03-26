def containers(pos, vol):
    global c, take, liters

    if vol < 0:
        return 0
    if pos == len(c):
        if vol == 0 and sum(take) == 4:
            return 1
        else:
            return 0
    
    take[pos] = 0
    count = containers(pos+1, vol)
    take[pos] = 1
    count += containers(pos+1, vol-c[pos])
    return count
    
liters = 150

f = open('input.txt', 'r')
c = []
for line in f:
    c.append(int(line))
take = [0]*len(c)
f.close()

#minimal number of containers is 4
print(containers(0, liters))