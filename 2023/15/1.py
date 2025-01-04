def HASH(s):
    hash = 0
    for c in s:
        hash += ord(c)
        hash *= 17
        hash %= 256

    return hash

f = open('input.txt', 'r')

lines = [line.strip() for line in f]
line = lines[0]
strings = line.split(',')

sum = 0
for string in strings:
    sum += HASH(string)

print(sum)