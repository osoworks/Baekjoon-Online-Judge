n, m = map(int, input().split())
x = [0] * (n+1)

for a in range(m):
	i, j, k = map(int, input().split())
	for b in range(i, j+1):
		x[b] = k

for i in range(1, n+1):
	print(x[i], end=" ")