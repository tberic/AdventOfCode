class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

n = 3012210
a = Node(1)
beg = a

for i in range(2, n+1):
    a.next = Node(i)
    a = a.next
    if i == n//2: # one before the first one to be erased
        b = a
#make a circular list
a.next = beg
a = a.next

while n > 1:
    b.next = b.next.next
    n -= 1
    
    # advance b (if needed)
    if n%2 == 0:
        b = b.next
        
print(b)