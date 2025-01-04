class Node:
    def __init__(self):
        self.data = []
        self.children = []

def createTree():
    global a, pos
    m = a[pos]
    n = a[pos+1]
    pos += 2
    
    node = Node()
    
    for i in range(m):
        node.children.append(createTree())        
    for j in range(n):
        node.data.append(a[pos+j])
    pos += n

    #print(pos)

    return node

def printTree(node):
    if not node.data:
        return
    
    print('Data: ', end='')
    for x in node.data:
        print(x, end=' ')
    print()
    print('Children: ')
    for n in node.children:
        printTree(n)

def value(node):    
    if not node.data:
        return 0

    if not node.children:
        sum = 0
        for x in node.data:
            sum += x
        return sum

    sum = 0
    for x in node.data:
        if x-1 in range(len(node.children)):
            sum += value(node.children[x-1])
    return sum


f = open('input.txt', 'r')
a = list(map(int, f.readline().split()))
f.close()

pos = 0
root = createTree()

print(value(root))