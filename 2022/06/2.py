def different(str):
    l = list(str)
    l.sort()
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            return False
    return True

fin = open('input.txt', 'r')

for line in fin:
    for j in range(13, len(line)):
        if different(line[j-13:j+1]):
            print(j+1)
            break
