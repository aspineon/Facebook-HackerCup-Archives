'''
Author : Prateek Chanda(@prateekiiest)
Problem Link: https://www.facebook.com/hackercup/problem/589264531559040/
Explanation: Under explanation folder
'''

def perform_operation(first, sec, op):
	if op == "|":
		
		if first == "X" and sec == "x":
			return "1"
		elif first == "x" and sec == "X":
			return "1"
		elif first == "X" and sec == "1":
			return "1"
		elif first == "1" and sec == "X":
			return "1"
		elif first == "x" and sec  == "1":
			return "1"
		elif first == "1" and sec == "x":
			return "1"
		elif first == "x" and sec == "x":
			return "x"
		elif first == "X" and sec == "X":
			return "X"	
		elif first == "X" and sec == "0":
			return "X"
		elif first == "0" and sec == "X":
			return "X"
		elif first == "x" and sec  == "0":
			return "x"
		elif first == "0" and sec == "x":
			return "x"
		elif first == "0" and sec == "1":
			return "1"
			
		elif first == "1" and sec == "0":
			return "1"
			
		elif first == "1" and sec == "1":
			return "0"
		elif first == "0" and sec == "0":
			return "0"
			
			
			
	elif op == "&":
		
		
		if first == "X" and sec == "x":
			return "0"
		elif first == "x" and sec == "X":
			return "0"
		elif first == "x" and sec == "x":
			return "x"
		elif first == "X" and sec == "X":
			return "X"
		elif first == "X" and sec == "1":
			return "X"
		elif first == "1" and sec == "X":
			return "X"
		elif first == "x" and sec  == "1":
			return "x"
		elif first == "1" and sec == "x":
			return "x"
			
		elif first == "X" and sec == "0":
			return "0"
		elif first == "0" and sec == "X":
			return "0"
		elif first == "x" and sec  == "0":
			return "0"
		elif first == "0" and sec == "x":
			return "0"
			
		elif first == "0" and sec == "1":
			return "0"
			
		elif first == "1" and sec == "0":
			return "0"
			
		elif first == "1" and sec == "1":
			return "1"
		elif first == "0" and sec == "0":
			return "0"
			
	
	# XOR operator		
	elif op == "^":
		if first == "X" and sec == "x":
			return "1"
		elif first == "x" and sec == "X":
			return "1"
		elif first == "x" and sec == "x":
			return "0"
		elif first == "X" and sec == "X":
			return "0"
		elif first == "X" and sec == "1":
			return "x"
		elif first == "1" and sec == "X":
			return "x"
		elif first == "x" and sec  == "1":
			return "X"
		elif first == "1" and sec == "x":
			return "X"
			
		elif first == "X" and sec == "0":
			return "X"
		elif first == "0" and sec == "X":
			return "X"
		elif first == "x" and sec  == "0":
			return "x"
		elif first == "0" and sec == "x":
			return "x"
			
		elif first == "0" and sec == "1":
			return "1"
			
		elif first == "1" and sec == "0":
			return "1"
			
		elif first == "1" and sec == "1":
			return "0"
		elif first == "0" and sec == "0":
			return "0"
		
		# do it later
			
operand_values = ["1","0", "X", "x"]
operator_values = ["|", "&", "^"]

t = int(input())

for test in range(t):
	exp = input()

	operator = []
	operand =  []

	cnt = 0
	for k in exp:
		if k == "(":
			cnt += 1
		
			
		
		if k in operand_values:
			operand.append(k)
		
		if k in operator_values:
			operator.append(k)
			
			
		if k  ==  ")":
			first = operand.pop()
			second = operand.pop()
			op = operator.pop()
			val = perform_operation(first,second,op)
			operand.append(val)
			cnt  -= 1
			
	c = operand.pop()
	
	change = 0
	if c == "1" or c == "0":
		change = 0
	else:
		change = 1
		
			
	print("Case #" + str(test+1) + ": "+str(change))
