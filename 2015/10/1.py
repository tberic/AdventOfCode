f = open('input.txt', 'r')
x = f.readline().strip()
f.close()

#print(x)
for step in range(50):
    y = ""
    i = 0
    while i < len(x):
        j = i
        while j < len(x) and x[j] == x[i]:
            j += 1
        y += str(j-i) + str(x[i])
        i = j
    x = y
    #print(x)
    print(step)

print(len(x))