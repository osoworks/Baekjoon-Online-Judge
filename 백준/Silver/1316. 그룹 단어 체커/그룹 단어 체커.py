n = int(input())
t = n

for i in range(n) :
	x = input()

	for j in range(len(x)-1):
		if x[j] == x[j+1] :
			continue
		elif x[j] in x[j+1:]:
			t -= 1
			break

print(t)