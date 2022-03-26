from operator import mul
from functools import reduce

def parse(s):
    global i
    num = 0
    a = []
    ver = int(msg[i:i+3], 2)
    print('Packet ver: ' + str(ver), end=' ')
    i += 3
    typeID = int(msg[i:i+3], 2)
    i += 3
    print('TypeID: ' + str(typeID), end=' ')
    if typeID == 4:
        leading = 1
        packet = ""
        while leading == 1:
            leading = int(msg[i], 2)
            i += 1
            packet += msg[i:i+4]
            i += 4
        num = int(packet, 2)
        print('Int literal: ' + str(num), end=' ')

    else:
        ltID = int(msg[i], 2)
        print('lTypeID: ' + str(ltID), end=' ')
        i += 1
        if ltID == 0:
            length = int(msg[i:i+15], 2)
            print('Length: ' + str(length), end=' ')
            i += 15
            j = i
            while i-j < length:
                a.append(parse(s))
        else:
            nPackets = int(msg[i:i+11], 2)
            print('nPackets: ' + str(nPackets), end=' ')
            i += 11
            for _ in range(nPackets):
                a.append(parse(s))
    print()

    if typeID == 0:
        return sum(a)
    elif typeID == 1:
        return reduce(mul, a, 1)
    elif typeID == 2:
        return min(a)
    elif typeID == 3:
        return max(a)
    elif typeID == 5:
        return int(a[0] > a[1])
    elif typeID == 6:
        return int(a[0] < a[1])
    elif typeID == 7:
        return int(a[0] == a[1])

    return num

f = open('input.txt', 'r')
line = f.readline().strip()
#line= "C200B40A82"

msg_hex = [c for c in line]
msg = "".join([ format(int(x, 16), "04b") for x in msg_hex ])

#g = open('msg.txt', 'w')
#print(msg, file=g)
#g.close()

i = 0
print(parse(msg))

f.close()