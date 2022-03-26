def QE():
    global w, used
    p = 1
    for i in range(len(w)):
        if used[i] == 1:
            p *= w[i]
    return p

def sumTarget(n, target):
    global w, used, minQE

    if target < 0:
        return False

    if target == 0:
        q = QE()        
        if q < minQE:
            minQE = q
            print(q)

    if n <= 0:
        return False

    for i in range(len(w)-1, -1, -1):
        if not used[i]:
            used[i] = 1
            sumTarget(n-1, target-w[i])
            used[i] = 0
    return False

f = open('input.txt', 'r')
w = [int(line.strip()) for line in f]
f.close()
target = sum(w)//3
#target = 516

used = [0] * len(w)
N = 6 #minimal number of packets in the first group
minQE = 10**40
sumTarget(N, target)
print(minQE)