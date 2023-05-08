#방법 1
x = list(str(input()))

if list(reversed(x)) == x:
	print(1)
else:
	print(0)

#방법 2
#x = input()
#print(1 if x == x[::-1] else 0)