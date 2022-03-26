# for a given n find n elemets from the sequence that sum to a target number
# calculate the minimal QE for all sets of n elements that sum to the target

def QE():
    global w, used
    p = 1
    for i in range(len(w)):
        if used[i] == 1:
            p *= w[i]
    return p

def balance(n, target):
    global w, used, minQE
    
    if target < 0:
        return False

    if target == 0:
        q = QE()
        if q < minQE:
            minQE = q
        return True

    if n <= 0:
        return False
    
    for i in range(len(w)-1, -1, -1):
        if not used[i]:
            used[i] = 1
            balance(n-1, target - w[i])
            used[i] = 0


f = open('input.txt', 'r')
w = [int(line.strip()) for line in f]
f.close()

target = sum(w)//4
used = [0] * len(w)

minQE = 10**30
n = 5
balance(n, target)
print(minQE)