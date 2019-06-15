# your code goes here


def sumSquare(n):

	low , high  = 0, 46341  # high = sqrt(2^31)
	cnt  = 0
	
	while(low<=high):
		p  = low*low + high*high
		if p > n:
			high -= 1
		elif p < n:
			low += 1
		else:
			cnt += 1
			low += 1
		
		
	
	return cnt
	
	
t = input()
for k in range(t):
	n = int(input())
	c = sumSquare(n)
	print("Case #" + str(k+1) + ": "+str(c))
