def solve(n):
    a = [12, 10, 10, -6, 11, -12, 11, 12, 12, -2, -5, -4, -4, -12]
    b = [6, 2, 13, 8, 13, 8, 3, 11, 10, 8, 14, 6, 8, 2]
    c = [1, 1, 1, 26, 1, 26, 1, 1, 1, 26, 26, 26, 26, 26]
    
    x, y, z, w = (0, 0, 0, 0)
    for i in range(14):
        d = int(str(n)[i])
        x = z % 26 + a[i]
        z //= c[i]
        if x != d:
            z = z*26 + d + b[i]
        print(d, x, z)

    return z
    


n = 98299999999999
solve(n)
#while solve(n):
    
#   print(n)
#   n -= 1
#   while '0' in str(n):
#       n -= 1
