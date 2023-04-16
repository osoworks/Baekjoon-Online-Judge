x = int(input())
y = list(map(int, input().split()))

#방법 1
print(min(y), max(y))

#방법 2
#a = y[0] #최소값
#b = y[0] #최대값

#for i in y: 
#for i in range(x): 로 대체 가능
#	if i > a:
#		a = i
#	elif i < min:
#		b = i

#방법 3
#z = sorted(y)
#print(z[0], z[-1])