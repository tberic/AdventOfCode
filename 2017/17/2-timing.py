from time import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


x = 369

l = Node(0)
l.next = l

t1 = time()

N = 1000000
for i in range(1, N+1):
    for _ in range(x):
        l = l.next

    t = Node(i)
    t.next = l.next
    l.next = t
    l = t

t2 = time()

print('Created a list: ' + str(t2-t1) + ' s')


#find zero
while l.data != 0:
    l = l.next

print(l.next.data)

t3 = time()
print('Found zero: ' + str(t3-t2) + ' s')
