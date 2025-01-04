import hashlib

f = open('input.txt', 'r')
hashKey = f.readline().strip()
f.close()
#hashKey = "pqrstuv"

for i in range(10**7):
    result = hashlib.md5((hashKey+str(i)).encode()).hexdigest()
    if result[:5] == "00000":
        print(i)
        break