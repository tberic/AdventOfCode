from itertools import combinations
import heapq

def state(floor, cur, n):
    res = 0
    for i in range(len(floor)):
        pairs, chips, gens = (0, 0, 0)
        for x in floor[i]:
            if -x in floor[i]:
                pairs += 1
            elif x > 0:
                chips += 1
            else:
                gens += 1
        t = pairs * (N+1)**2 + chips * (N+1) + gens
        res = res*10**3 + t
    return res*10+cur


def check(floor, f, g):
    for x in floor[f]:
        if x > 0:
            if -x in floor[f]:
                continue
            if any(n < 0 for n in floor[f]):
                return False
    for x in floor[g]:
        if x > 0:
            if -x in floor[g]:
                continue
            if any(n < 0 for n in floor[g]):
                return False
    return True

def lower(f):
    for i in range(f):
        if floor[i]:
            return True
    return False


def priority(floor):
    s = 0
    for f in range(4):
        s += len(floor[f])*(3-f)
    return s


# microchips are positive numbers, corresponding generators are corresponding negative numbers
startingFloor = [
            [1, 2, 3, -1, -2, -3, -4, -5, 6, -6, 7, -7],
            [4, 5],
            [],
            []
        ]
N = 7

# startingFloor = [
#             [1, 2, 3, -1, -2, -3, -4, -5],
#             [4, 5],
#             [],
#             []
#         ]
# N = 5


# startingFloor = [
#             [1, 2],
#             [-1],
#             [-2],
#             []
#         ]

cost = {}

Q = []
heapq.heappush(Q, (priority(startingFloor), startingFloor, 0, 0) )

while Q:
    pq, floor, f, steps = heapq.heappop(Q)

    s = state(floor, f, N)
    if s not in cost:
        cost[s] = steps
    elif steps < cost[s]:
        cost[s] = steps
    else:
        continue

    if len(floor[0]) == 0 and len(floor[1]) == 0 and len(floor[2]) == 0:
        print(f'Solved! {steps}')

    #print(steps, f, floor)

    # going up
    if f < 3:
        # two items go on the elevator
        for x, y in combinations(floor[f], 2):
            if (x*y < 0 and x != -y):
                continue
            else:
                newFloor = [row[:] for row in floor]
                newFloor[f].remove(x)
                newFloor[f].remove(y)
                newFloor[f+1].append(x)
                newFloor[f+1].append(y)
                if check(newFloor, f, f+1):
                    heapq.heappush(Q, (priority(newFloor), newFloor, f+1, steps+1) )

        # one item goes on the elevator
        for x in floor[f]:
            newFloor = [row[:] for row in floor]
            newFloor[f].remove(x)
            newFloor[f+1].append(x) 
            if check(newFloor, f, f+1):
                heapq.heappush(Q, (priority(newFloor), newFloor, f+1, steps+1) )


    # going down
    if f > 0 and lower(f):
        for x in floor[f]:
            newFloor = [row[:] for row in floor]
            newFloor[f].remove(x)
            newFloor[f-1].append(x) 
            if check(newFloor, f, f-1):
                heapq.heappush(Q, (priority(newFloor), newFloor, f-1, steps+1) )

print(cost[ state([[], [], [], [1, 2, 3, 4, 5, 6, 7, -1, -2, -3, -4, -5, -6, -7]], 3, N) ])
#print(cost[ state([[], [], [], [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]], 3, N) ])