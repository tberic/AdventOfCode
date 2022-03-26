class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

def parseInput(s):
    if len(s) == 1:
        return Node(int(s))

    #found the middle comma
    pos = 1
    brackets = 0
    if s[pos] == '[':
        brackets = 1
    while brackets:
        pos += 1
        if s[pos] == '[':
            brackets += 1
        elif s[pos] == ']':
            brackets -= 1

    root = Node(-1)
    root.left = parseInput(s[1:pos+1])
    root.right = parseInput(s[pos+2:-1])
    return root

def joinTrees(l, r):
    root = Node(-1)
    root.left = l
    root.right = r
    return root

#postorder
def strTree(n):
    if n is None:
        return ""
    if n.data != -1:
        return str(n.data)
    return '['+strTree(n.left) + ',' + strTree(n.right)+']'
    #print(n.data, end=' ')
    #printTree(n.left)
    #printTree(n.right)

def reduceExplode(n, depth):
    if n is None:
        return None
    
    if n.data == -1 and depth == 4:
        x = n.left.data
        y = n.right.data
        n.data = 0
        n.left = None
        n.right = None
        return (x, y)
        
    res = reduceExplode(n.left, depth+1)
    if res:
        x, y = res
        if y > 0:
            p = n.right
            while p.data == -1:
                p = p.left
            p.data += y
            y = 0
        return (x, y)
    
    res = reduceExplode(n.right, depth+1)
    if res:
        x, y = res
        if x > 0:
            p = n.left
            while p.data == -1:
                p = p.right
            p.data += x
            x = 0
        return (x, y)

    return None
    
def magnitude(n):
    if n.data == -1:
        return 3*magnitude(n.left) + 2*magnitude(n.right)
    elif n.data:
        return n.data
    else:
        return 0

def reduceSplit(n):
    if n is None:
        return False

    if n.data >= 10:
        if n.data % 2 == 0:
            x, y = (n.data//2, n.data//2)
        else:
            x, y = (n.data//2, n.data//2+1)
        n.data = -1
        n.left = Node(x)
        n.right = Node(y)
        return True
    
    res = reduceSplit(n.left)
    if res:
        return True
    return reduceSplit(n.right)

def addTrees(l, r):
    if l.data is None:
        return r
    if r.data is None:
        return l

    root = joinTrees(l, r)
    res = 1
    while res:
        res = reduceExplode(root, 0)
        while res:
            res = reduceExplode(root, 0)
        res = reduceSplit(root)
    return root


f = open('input.txt', 'r')
lines = [line.strip() for line in f]

maxMag = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if i != j:
            a = parseInput(lines[i])
            b = parseInput(lines[j])
            x = magnitude(addTrees(a, b))
            maxMag = max(maxMag, x)
        

print(maxMag)

f.close()