def findReaction(s, pos):
    while pos < len(s)-1 and abs(ord(s[pos])-ord(s[pos+1])) != 32:
        pos += 1
    if pos == len(s)-1:
        return -1
    return pos


f = open('input.txt', 'r')
polymer = f.readline().strip()
f.close()

#polymer = "dabAcCaCBAcCcaDA"
pos = findReaction(polymer, 0)
while pos != -1:
    #print(pos, polymer)
    polymer = polymer[:pos] + polymer[pos+2:]
    pos = findReaction(polymer, max(pos-1, 0))
    
#print(polymer)
      







print(len(polymer))