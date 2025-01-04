fil = open('input.txt', 'r')

def countChar(c, digits):
	count = 0
	for d in digits:
		if (c in d):
			count +=1
	return count

def nadji(c, s):
	for i in range(len(s)):
		if (c == s[i]):
			return i

def toNum(s):
	if (len(s) == 7):
		return 8
	if (len(s) == 4):
		return 4
	if (len(s) == 3):
		return 7
	if (len(s) == 2):
		return 1
		
	if (len(s) == 6):
		if ('d' not in s):
			return 0
		if ('c' not in s):
			return 6
		if ('e' not in s):
			return 9
		
	if ('b' not in s and 'f' not in s):
		return 2
	if ('b' not in s and 'e' not in s):
		return 3
	if ('c' not in s and 'e' not in s):
		return 5
	
        

sum = 0
for line in fil:
	input = line.split(' | ')[0]
	y = input.split(' ')
	y.sort(key=len)
	x = [set() for i in range(10)]
	x[1] = set(y[0])
	x[7] = set(y[1])
	x[4] = set(y[2])
	
	for ch in x[1]:
		if (countChar(ch, y) == 9):
			f = ch
		
	for ch in 'abcdefg':
		if (countChar(ch, y) == 4):
			e = ch
		elif (countChar(ch, y) == 6):
			b = ch
			
	for i in range(9):
		if (f not in y[i]):
			x[2] = set(y[i])
			break

	c = list(x[1] & x[2])[0]
	d = list((x[2] & x[4]) - set(c))[0]
	a = list((x[2] & x[7]) - set(c))[0]
	g = list(set('abcdefg') - set(a+b+c+d+e+f))[0]
	dig = [a, b, c, d, e, f, g]
        
	#print(a+b+c+d+e+f+g)
        
	output = line.split(' | ')[1]
	output = output[:-1]
        
	number = 0
	for s in output.split(' '):
		t = [chr(nadji(s[i],dig)+ord('a')) for i in range(len(s))]
		num = toNum(t)
		number = number*10 + num
	sum += number


print(sum)

fil.close()