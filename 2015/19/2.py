#takes too long to run, but finds the minimal number of steps right at the beginning
sol = {}

def solve(s, k):
    global reduce, minSteps, sol

    if k >= minSteps:
        return None

    if s == 'e':
        minSteps = k
        print('Found it: ' + str(k))
        return k

    if 'e' in s:
        return None
   
    if s in sol:
        return sol[s]

    minCur = 10**20
    for x in reduce:
        pos = s.find(x)
        while pos != -1:
            m = solve(s[:pos] + reduce[x] + s[pos+len(x):], k+1)
            if m and m-k < minCur:
                minCur = m-k
            pos = s.find(x, pos+1)

    sol[s] = minCur
    return minCur


f = open('input.txt', 'r')

lines = [line.strip() for line in f]
medicine = lines[-1]
reduce = {}
for x in lines[:-2]:
    a, b = x.split(' => ')
    reduce[b] = a
f.close()

minSteps = 10**20
solve(medicine, 0)
print(minSteps)