def ispis(l):
    a = l.next
    print(l.data, end='->')
    while a != l:
        print(a.data, end='->')
        a = a.next
    print()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


x = 369

l = Node(0)
l.next = l

N = 2017
for i in range(1, N+1):
    for _ in range(x):
        l = l.next

    t = Node(i)
    t.next = l.next
    l.next = t
    l = t

    #print(l.data, end=': ')
    #ispis(l)

print(l.next.data)