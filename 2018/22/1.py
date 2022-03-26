draw = ['.', '=', '|']

def riskLevel(index):
    return index%3

def erosionLevel(index):
    global depth
    return (index + depth) % M

M = 20183

depth = 6969
targetx = 9
targety = 796

# depth = 510
# targetx = 10
# targety = 10


row = [ erosionLevel( x*16807 ) for x in range(targetx+1) ]
risk = sum(map(riskLevel, row))

#print("".join([draw[riskLevel(x)] for x in row]))

for y in range(1, targety+1):
    row[0] = erosionLevel( y*48271 )
    for x in range(1, targetx+1):
        row[x] = erosionLevel( row[x]*row[x-1] )
    
    risk += sum(map(riskLevel, row))
    #print("".join([draw[riskLevel(x)] for x in row]))
        
risk -= riskLevel(row[targetx])
risk += riskLevel(0)

print(risk)