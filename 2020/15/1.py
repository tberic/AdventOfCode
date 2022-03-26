f = open('input.txt')
l = list(map(int, f.readline().split(',')))
f.close()

last = {}
for i in range(len(l)):
    last[l[i]] = i

i = len(l)
lastNum = 0
#i < 2019
#30000000
while i < 30000000-1:
    if lastNum in last:
        newlastNum = i-last[lastNum]
    else:
        newlastNum = 0
   
    last[lastNum] = i
    lastNum = newlastNum
    i += 1

#print(last)
print(lastNum)