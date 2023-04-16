n, m = map(int, input().split())
x = [i for i in range(1,n+1)]

for a in range(m):
	i, j = map(int, input().split())
	y = x[i-1]
	x[i-1] = x[j-1]
	x[j-1] = y
	#x[i-1], x[j-1] = x[j-1], x[i-1]로 대체 가능

for i in range(n):
	print(x[i], end=" ")