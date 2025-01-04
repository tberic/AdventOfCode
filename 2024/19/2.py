from functools import lru_cache 

@lru_cache(maxsize=1000000)
def ways(target):
    if target == "":
        return 1
    
    total = 0
    for design in designs:
        if target.endswith(design):
            total += ways(target[:len(target) - len(design)])
            
    return total

f =  open('input.txt')

lines = [line.strip() for line in f]
designs = lines[0].split(', ')

total = 0
for i in range(2, len(lines)):
    print(i)
    target = lines[i]
    
    total += ways(target)        

print(total)