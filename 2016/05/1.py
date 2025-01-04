import hashlib

ID = "cxdnnyjw"

cnt = 0
while cnt < 8:
    for i in range(10**10):
        result = hashlib.md5((ID+str(i)).encode()).hexdigest()
        if result[:5] == "00000":
            print(result[5], end = '')
            cnt += 1
            if cnt == 8:
                break            