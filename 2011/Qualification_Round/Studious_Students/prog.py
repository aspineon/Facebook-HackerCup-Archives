
t = int(input())
for k in range(t):
	st = raw_input().split()
	n = int(st[0])
	p = sorted(st[1:])
	c = ''.join(p)
	print("Case #" + str(k+1) + ": "+str(c))
