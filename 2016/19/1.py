import math

def seq(start, end, step):
    l = int( math.ceil((end-start)/step) )

    if l <= 1:
        return start

    if l % 2 == 0:
        return seq(start, end, step*2)

    return seq(start+step*2, end, step*2)

n = 3012210
print( seq(1, n+1, 1) )