a,b = map(int, input().split())
x = list(map(int, input().split()))

#방법 1
for i in range(a):
	if x[i] < b:
		print(x[i], end=" ")

#방법 2
#for i in x:
#	if i < b:
#		print(i, end= " ")