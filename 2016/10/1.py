f = open('input.txt', 'r')

lines = [line.strip() for line in f]

# find the highest bot number
nBot = 0
for line in lines:
    words = line.split()
    x = int(words[1])
    if x > nBot:
        nBot = x
#print(nBot)

# highest bot number is 209
# highest output number is 20 (manual search of the input file)

bot = [ [] for i in range(nBot+1) ]
botWait = [-1 for i in range(nBot+1)]
output = [0 for i in range(21)]
done = [0 for i in range(len(lines))]

i = 0
while not all(done):
    if i >= len(lines):
        i = 0
    
    if done[i]:
        i += 1
        continue

    #print(lines[i])

    words = lines[i].split()
    
    if words[0] == "bot":
        ID = int(words[1])
        if len(bot[ID]) == 2:
            done[i] = 1

            if bot[ID] == [61, 17]:
                print(ID)

            x = int(words[6])
            y = int(words[11])
            if words[5] == "bot":
                bot[x].append( min(bot[ID]) )
            else:
                output[x] = min(bot[ID])

            if words[10] == "bot":
                bot[y].append( max(bot[ID]) )
            else:
                output[y] = max(bot[ID])

            bot[ID].clear()
            
            if words[5] == "bot":
                i = min(i, botWait[x])
            if words[10] == "bot":
                i = min(i, botWait[y])
        else:
            botWait[ID] = i
    elif words[0] == "value":
        done[i] = 1
        x = int(words[1])
        ID = int(words[5])
        bot[ID].append(x)
        if len(bot[ID]) == 2:
            i = botWait[ID]
    
    i += 1

print(output[0]*output[1]*output[2])

f.close()