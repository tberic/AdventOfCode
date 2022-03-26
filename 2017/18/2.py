f = open('input.txt', 'r')
lines = [line.strip() for line in f]
f.close()

cnt = [0, 0]
i = [0, 0]
waiting = [0, 0]
finished = [0, 0]
reg = [{'p': 0}, {'p': 1}]
output = [[], []]
ID = 0 #start with program 0 and then alternate
while True:
    if finished[0] and finished[1]:
        break

    if i[ID] < 0 or i[ID] >= len(lines):
        finished[ID] = 1
        ID=1-ID
        continue

    print(ID, i[ID], lines[i[ID]], reg[ID], waiting, finished, len(output[0]), len(output[1]))

    if waiting[0] and waiting[1] and (not output[0]) and (not output[1]):
        break
    if waiting[ID] and finished[1-ID]:
        break

    if waiting[ID] and (not output[ID]):
        ID = 1-ID
        continue
    

    instr, *l = lines[i[ID]].split()

    if l[0][0] in '-0123456789':
        a = int(l[0])
    else:
        a = l[0]
        if a not in reg[ID]:
            reg[ID][a] = 0
    
    if len(l) == 2:
        if l[1][0] in '-0123456789':
            b = int(l[1])
        else:
            b = reg[ID][l[1]]

    if instr == "snd":
        cnt[ID] += 1

        if l[0][0] in '-0123456789':
            output[1-ID].append(a)
        else:
            output[1-ID].append(reg[ID][a])
    elif instr == "set":
        reg[ID][a] = b
    elif instr == "add":
        reg[ID][a] += b
    elif instr == "mul":
        reg[ID][a] *= b
    elif instr == "mod":
        reg[ID][a] %= b
    elif instr == "rcv":
        if output[ID]:
            waiting[ID] = 0
            reg[ID][a] = output[ID].pop(0)
        else:
            waiting[ID] = 1
            ID = 1-ID
            continue
    elif instr == "jgz":
        if l[0][0] in '-0123456789':
            if a > 0:
                i[ID] += b
                #ID = 1-ID
                continue
        else:
            if reg[ID][a] > 0:
                i[ID] += b
                #ID = 1-ID
                continue
    i[ID] += 1
    if not finished[1-ID]:
        ID = 1-ID

print(cnt)