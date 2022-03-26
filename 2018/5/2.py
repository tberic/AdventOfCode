def findReaction(s, pos):
    while pos < len(s)-1 and abs(ord(s[pos])-ord(s[pos+1])) != 32:
        pos += 1
    if pos == len(s)-1:
        return -1
    return pos


f = open('input.txt', 'r')
polymerOriginal = f.readline().strip()
f.close()

#{polymerOriginal = "dabAcCaCBAcCcaDA"

minLen = len(polymerOriginal)
minc = 0
for c in range(26):
    if (chr(c+65) in polymerOriginal) or (chr(c+97) in polymerOriginal):
        polymer = polymerOriginal
        polymer = polymer.replace(chr(c+65), "")
        polymer = polymer.replace(chr(c+97), "")
        #polymer = removePair(polymer, chr(c+65), chr(c+97))
        #print(chr(c+65), chr(c+97), polymer)

        pos = findReaction(polymer, 0)
        while pos != -1:        
            polymer = polymer[:pos] + polymer[pos+2:]
            pos = findReaction(polymer, max(pos-1, 0))

        if len(polymer) < minLen:
            minLen = len(polymer)
            minc = c
      
print(minLen, minc)