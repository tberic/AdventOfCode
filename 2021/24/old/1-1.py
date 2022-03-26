def solve(n):
    a = [12, 10, 10, -6, 11, -12, 11, 12, 12, -2, -5, -4, -4, -12]
    b = [6, 2, 13, 8, 13, 8, 3, 11, 10, 8, 14, 6, 8, 2]
    c = [1, 1, 1, 26, 1, 26, 1, 1, 1, 26, 26, 26, 26, 26]
    
    x, y, z, w = (0, 0, 0, 0)
    for i in range(14):
        d = int(n[i])
        x = z % 26 + a[i]
        z //= c[i]
        if x != d:
            z = z*26 + d + b[i]
        #print(z)

    return z
    


# n = "99988999999999"
# #solve(n)
# while solve(n):
#     print(n)

class BreakIt(Exception): pass

n = "991889999xxxxx"
try:

    for i10 in range(9, 0, -1):
        for i11 in range(9, 0, -1):
            for i12 in range(9, 0, -1):
                for i13 in range(9, 0, -1):
                    for i14 in range(9, 0, -1):
                        s = n[:9] + \
                            chr( ord('0')+i10 ) + chr( ord('0')+i11 ) + chr( ord('0')+i12 ) + \
                            chr( ord('0')+i13 ) + chr( ord('0')+i14 )
                        n = s
                        print(n)
                        if not solve(n):
                            raise BreakIt
except BreakIt:
    pass