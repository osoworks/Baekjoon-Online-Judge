#방법 1
u = -1

for i in range(9):
    a = list(map(int, input().split()))
    if max(a) > u:
        u = max(a)
        x = i + 1
        y = a.index(u) + 1
print(u)
print(x,y)

#방법 2
#x = []

#for i in range(9):
#	x.append(list(map(int, input().split())))
#x = [list(map(int, input().split())) for _ in range(9)]로 대체 가능

#a = 0
#b = 0
#u = -1

#for i in range(9):
#	for j in range(9):
#		for x[i][j] > u:
#			u = x[i][j]
#			a = i+1
#			b = j+1

#print(u)
#print(a,b)