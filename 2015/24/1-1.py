def sumTarget(n, target):
    global w, used, nGlobal

    if target < 0:
        return False

    if target == 0:
        print(used)
        m = 1
        while not sumTarget(m, 516) and m < len(w) - nGlobal:
            print(' '*10 + str(m))
            m += 1
        return True

    if n <= 0:
        return False

    for i in range(len(w)-1, -1, -1):
        if not used[i]:
            used[i] = 1
            res = sumTarget(n-1, target-w[i])
            if res:
                return True
            used[i] = 0
    return False


f = open('input.txt', 'r')
w = [int(line.strip()) for line in f]
f.close()
#target = sum(w)//3
target = 516

used = [0] * len(w)

nGlobal = 6
while not sumTarget(nGlobal, target):
    print(nGlobal)
    nGlobal += 1

print(used)