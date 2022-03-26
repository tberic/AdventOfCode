def spin(n):
    global s
    s = s[-n:] + s[:-n]

def exchange(i, j):
    global s
    t = list(s)
    c = t[i]
    t[i] = t[j]
    t[j] = c
    s = "".join(t)

def partner(a, b):
    global s
    exchange(s.find(a), s.find(b))


f = open('input.txt', 'r')
line = f.readline().strip()
f.close()

start = "".join([chr(i) for i in range(97, 113)])
s = start
N = 1000000000

#seen = set()

#there is a cycle of length 60
for _ in range(N%60):
    for instr in line.split(','):
        if instr[0] == "s":
            spin( int(instr[1:]) )
        elif instr[0] == "x":
            w = instr[1:].split('/')
            exchange( int(w[0]), int(w[1]) )
        elif instr[0] == "p":
            w = instr[1:].split('/')
            partner( w[0], w[1] )
    # if s in seen:
    #     break
    # seen.add(s)

print(s)

#work out the permutation
# p = [ s.find(c) for c in start ]
# print(p)

# for i in range(len(p)):
#     seen = [0 for i in range(16)]
#     print(i, end='->')
#     a = p[i]
#     while not seen[a]:
#         print(a, end='->')
#         seen[a] = 1
#         a = p[a]    
#     print()
        