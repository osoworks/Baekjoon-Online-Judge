x = int(input())
y = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(x):
	a,b = map(int, input().split())
	for i in range(a, a+10):
		for j in range(b, b+10):
			y[i][j] = 1
	#for i in range(10): for j in range(10): y[a+i][b+j] = 1로 대체 가능

z = 0

for t in y:
	z += t.count(1)
print(z)