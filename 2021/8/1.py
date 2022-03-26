f = open('input.txt', 'r')

count = 0
for line in f:
        output = line.split(' | ')[1]
        #print(output)
        output = output[:-1]
        for s in output.split(' '):                
                if (len(s) == 2 or len(s) == 3 or len(s) == 4 or len(s) == 7):
                        count += 1

print(count)

f.close()
