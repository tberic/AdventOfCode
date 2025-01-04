nPlayers = 486
nMarbles = 7083300

#nPlayers = 30
#nMarbles = 5807

score = [0 for i in range(nPlayers)]

class Node:
	def __init__(self, x=0):
		self.x = x
		self.next = None
		self.prev = None

root = Node()
root.next = root
root.prev = root
cur = root

for i in range(1, nMarbles+1):
	if i % 23 == 0:
		score[i%nPlayers] += i
		for j in range(7):
			cur = cur.prev
		score[i%nPlayers] += cur.x
		before = cur.prev		
		after = cur.next
		before.next = after
		after.prev = before
		cur = after						
	else:
		before = cur.next
		after = cur.next.next
		n = Node(i)
		before.next = n
		n.next = after
		n.prev = before
		after.prev = n
		cur = n
		
		
#n = root
#while n.next != root:
#	print(n.x, end = ' ')
#	n = n.next

print(max(score))
