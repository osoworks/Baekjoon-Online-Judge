import sys
input = sys.stdin.readline

a, b = map(int, input().split())
x = []
y = 0

for i in range(1, a+1):
	if a % i == 0:
		x.append(i)
	y += 1

if b > len(x):
	print(0)
else:
	print(x[b-1])