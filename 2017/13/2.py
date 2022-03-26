f = open('input.txt', 'r')
ran = { int(line.split(': ')[0]): int(line.split(': ')[1]) for line in f }
n = max(ran.keys())
f.close()

#if we analyze the input file, we see that we have to have delay%26 == 12
#added other conditions, now it's blisteringly fast
delay = 12
while True:
    delay += 26
    if delay % 14 != 6:
        continue
    if delay % 10 != 4:
        continue
    if delay % 6 != 2:
        continue

    print(delay)

    done = 1
    for j in range(n+1):
        if j in ran:
            if (delay+j) % (2*(ran[j]-1)) == 0:
                done = 0
                break
    if done:
        break    