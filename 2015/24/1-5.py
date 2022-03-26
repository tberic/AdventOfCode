def QE():
    global w, group
    p = 1
    for i in range(len(w)):
        if group[i] == 0:
            p *= w[i]
    return p

def balance(i):
    global w, group, target, bal, minQE
    
    if bal[0] > target or bal[1] > target:
        return False
    
    if bal[0] == target and bal[1] == target:
        q = QE()
        if q < minQE:
            minQE = q
            return True
        print(group, minQE)
        return False

    if i == len(w):
        return False

    if bal[0] < target:
        group[i] = 0
        bal[0] += w[i]
        balance(i+1)
        bal[0] -= w[i]
    
    if bal[1] < target:
        group[i] = 1
        bal[1] += w[i]
        balance(i+1)
        bal[1] -= w[i]

    if bal[2] < target:
        group[i] = 2    
        bal[2] += w[i]
        balance(i+1)
        bal[2] -= w[i]


f = open('input.txt', 'r')
w = [int(line.strip()) for line in f]
f.close()

target = sum(w)//3
group = [0] * len(w)
bal = [0] * len(w)

minQE = 10**30
balance(0)
print(minQE)