def calculate(ops, i, res, solution):
    if i == len(ops):
        return res == solution

    if res > solution:
        return False

    res1 = calculate(ops, i+1, res + ops[i], solution)
    if res1:
        return True
    res2 = calculate(ops, i+1, res * ops[i], solution)
    if res2:
        return True
    res3 = calculate(ops, i+1, int(str(res) + str(ops[i])), solution)
    if res3:
        return True

    return False


f = open('input.txt')

total = 0
for line in f:
    test, text = line.split(': ')
    operands = list(map(int, text.split(' ')))
    test = int(test)

    if calculate(operands, 0, 0, test):
        total += test

print(total)