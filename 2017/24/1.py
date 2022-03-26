def solve(last, strength):
    global tubes, used, maxStrength

    if strength > maxStrength:
        print('found max: ' + str(strength))
        maxStrength = strength

    for i, x in enumerate(tubes):
        if not used[i] and x[0] == last:
            used[i] = 1
            solve(x[1], strength + x[0] + x[1])
            used[i] = 0
        elif not used[i] and x[1] == last:
            used[i] = 1
            solve(x[0], strength + x[0] + x[1])
            used[i] = 0


f = open('input.txt', 'r')
tubes = [sorted(list(map(int, line.strip().split('/')))) for line in f]
f.close()

used = [0 for i in range(len(tubes))]
maxStrength = 0
solve(0, 0)