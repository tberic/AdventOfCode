f = open('input2.txt', 'r')
g = open('output.txt', 'w')

sum = 0
for line in f:
    room, ID = line.strip().split('-')
    ID = int(ID)
    
    decode = list(room)
    for i in range(len(room)):
        decode[i] = chr( ( ord(room[i])-ord('a') + ID )%26 + ord('a') )
    print("".join(decode) + ' ' + str(ID), file=g) 

f.close()
g.close()