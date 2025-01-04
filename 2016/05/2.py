import hashlib

ID = "cxdnnyjw"

password = list("_"*8)
while '_' in password:
    for i in range(10**20):
        result = hashlib.md5((ID+str(i)).encode()).hexdigest()
        if result[:5] == "00000" and result[5] in '01234567' and password[ int(result[5]) ] == '_':
            password[ int(result[5]) ] = result[6]
            print("".join(password))
            if '_' not in password:
                break