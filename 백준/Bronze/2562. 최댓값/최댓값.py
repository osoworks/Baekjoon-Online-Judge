x = []
for i in range(9):
	i = int(input())
	x.append(i)
print(max(x))
print(x.index(max(x))+1)