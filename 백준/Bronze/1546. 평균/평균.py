x = int(input())
y = list(map(int,input().split()))
z = max(y)

m = []

for i in y:
	m.append(i/z*100)

print(sum(m)/x)