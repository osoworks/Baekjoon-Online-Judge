n, m = map(int, input().split())
x = [i for i in range(1,n+1)]

for a in range(m):
	i, j = map(int, input().split())
	y = x[i-1:j]
	y.reverse()
	x[i-1:j] = y

for i in range(n):
	print(x[i], end=" ")