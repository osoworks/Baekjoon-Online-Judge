#방법 1
while True: #'True = 1'이므로 'while 1:'로 대체 가능
	a, b = map(int,input().split())
	if (a == 0 and b == 0):
		break
	print(a+b)

#방법 2
#while True: 
#	a, b = map(int,input().split())
#	if (a == 0 and b == 0):
#		break
#	else:
#		print(a+b)