a = [12, 10, 10, -6, 11, -12, 11, 12, 12, -2, -5, -4, -4, -12]
b = [6, 2, 13, 8, 13, 8, 3, 11, 10, 8, 14, 6, 8, 2]
c = [1, 1, 1, 26, 1, 26, 1, 1, 1, 26, 26, 26, 26, 26]

result = ""

def algoStep(z, d, i):
    global a, b, c
    x = z % 26 + a[i]
    z //= c[i]
    if x != d:
        z = z*26 + d + b[i]
    return z, x

def iterate(i, z):
    global a, b, c, result
    if i >= 14 and z == 0:
        print('found it')
        return True

    if i in [3, 5, 9, 10, 11, 12, 13]:
        if z % 26 + a[i] >= 10 or z % 26 + a[i] <= 0:
            return False
        t, x = algoStep(z, z % 26 + a[i], i)
        res = iterate(i+1, t)
        if res:
            #print(z % 26 + a[i], end='')
            result = str(z % 26 + a[i]) + result
        return res
    else:
        for k in range(1, 10):
            t, x = algoStep(z, k, i)
            res = iterate(i+1, t)
            if res:
                #print(k, end='')
                result = str(k) + result
                return True            

    return False
        
iterate(0, 0)
print(result)

# n = "x"*14
# try:

#     z = 0
#     for i1 in range(9, 0, -1):
#         n[0] = str(i1)
#         algoStep
#         for i2 in range(9, 0, -1):
#             n[1] = str(i2)
#             for i3 in range(9, 0, -1):
#                 n[2] = str(i3)                
#                 z = 0
#                 for i in range(3):
#                     d = int(n[i])
#                     x = z % 26 + a[i]
#                     z //= c[i]
#                     if x != d:
#                         z = z*26 + d + b[i]

#                 if z % 26 + a[3] >= 10:
#                     break
#                 n[3] = str(z % 26 + a[3])
                
#                 for i5 in range(9, 0, -1):
#                     n[4] = str(i5)

#                     for i7 in range(9, 0, -1):
#                         for i8 in range(9, 0, -1):
#                             for i9 in range(9, 0, -1):
                                
#                             chr( ord('0')+i13 ) + chr( ord('0')+i14 )
#                         n = s
#                         print(n)
#                         if not solve(n):
#                             raise BreakIt
# except BreakIt:
#     pass