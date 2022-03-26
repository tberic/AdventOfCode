f = open('input.txt', 'r')
count = 0
for line in f:
    words = line.strip().split()
    valid = 1
    for i in range(len(words)):
        if not valid:
            break
        for j in range(len(words)):
            if i != j and words[i] == words[j]:
                valid = 0
                break
    if valid:
        count += 1

f.close()

print(count)