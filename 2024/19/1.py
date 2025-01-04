from functools import lru_cache 

@lru_cache(maxsize=1000000)
def find(target):
    if target == "":
        return True
    for design in designs:
        if target.endswith(design):
            res = find(target[:len(target) - len(design)])
            if res:
                return True
            
    return False

f =  open('input.txt')

lines = [line.strip() for line in f]
designs = lines[0].split(', ')

total = 0
for i in range(2, len(lines)):
    print(i)
    target = lines[i]
    
    if find(target):
        total += 1

print(total)