def parsePacket(s, i):
    leading = 1
    packet = ""
    while leading == 1:
        leading = int(msg[i], 2)
        i += 1
        packet += msg[i:i+4]
        i += 4
    num = int(packet, 2)
    print('Int literal: ' + str(num), end=' ')
    # l = len(packet)
    # while l % 4 != 0:
    #     l += 1
    #     i += 1
    return i

def parse(s, i):
    print(i)
    global sum
    ver = int(msg[i:i+3], 2)
    print('Packet ver: ' + str(ver), end=' ')
    sum += ver
    i += 3
    typeID = int(msg[i:i+3], 2)
    i += 3
    print('TypeID: ' + str(typeID), end=' ')
    if typeID == 4:
        i = parsePacket(msg, i)
    else:
        ltID = int(msg[i], 2)
        print('lTypeID: ' + str(ltID), end=' ')
        i += 1
        if ltID == 0:
            length = int(msg[i:i+15], 2)
            print('Length: ' + str(length), end=' ')
            i += 15
            j = i
            while j-i < length:
                j = parse(s, j)
            i = j
        else:
            nPackets = int(msg[i:i+11], 2)
            print('nPackets: ' + str(nPackets), end=' ')
            i += 11
            for _ in range(nPackets):
                i = parse(s, i)
    #trailing zeros
    # while i % 4 != 0:
    #     i += 1

    print()
    return i

f = open('input.txt', 'r')
line = f.readline().strip()
#line= "EE00D40C823060"

msg_hex = [c for c in line]
msg = "".join([ format(int(x, 16), "04b") for x in msg_hex ])

#g = open('msg.txt', 'w')
#print(msg, file=g)
#g.close()

sum = 0
i = 0
while i < len(msg)-7:
    i = parse(msg, i)
    

print(sum)

f.close()