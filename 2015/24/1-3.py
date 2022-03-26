def sumTarget3(n, target):
    global w, used, N, M

    if target < 0:
        return False

    if target == 0:
        #print(' '*10 + str(used))
        return True

    if n <= 0:
        return False

    for i in range(len(w)-1, -1, -1):
        if not used[i]:
            used[i] = 3
            res = sumTarget2(n-1, target-w[i])
            if res:
                return True
            used[i] = 0
    return False

def sumTarget2(n, target):
    global w, used, N, M

    if target < 0:
        return False

    if target == 0:
        #print(used)
        m = 5
        print(' '*20 + str(m))
        while not sumTarget2(m, targetGlobal) and m < (len(w) - N - M)//2+1:
            m += 1
            print(' '*20 + str(m))
            
        if m == (len(w) - N - M)//2+1:
            return False
        return True

    if n <= 0:
        return False

    for i in range(len(w)-1, -1, -1):
        if not used[i]:
            used[i] = 2
            res = sumTarget2(n-1, target-w[i])
            if res:
                return True
            used[i] = 0
    return False


def sumTarget1(n, target):
    global w, used, N, targetGlobal

    if target < 0:
        return False

    if target == 0:
        #print(used)
        M = 5
        print(' '*10 + str(M))
        while not sumTarget2(M, targetGlobal) and M < (len(w) - N)//3+1:
            M += 1
            print(' '*10 + str(M))
            
        if M == (len(w) - N)//3+1:
            return False
        return True

    if n <= 0:
        return False

    for i in range(len(w)-1, -1, -1):
        if not used[i]:
            used[i] = 1
            res = sumTarget1(n-1, target-w[i])
            if res:
                return True
            used[i] = 0
    return False


f = open('input.txt', 'r')
w = [int(line.strip()) for line in f]
f.close()
targetGlobal = sum(w)//4
#target = 516

used = [0] * len(w)
N = 5
M = 5
sumTarget1(N, targetGlobal)
print(used)

# n = 6
# while not sumTarget1(nGlobal, target):
#     print(n)
#     n += 1

# print(used)