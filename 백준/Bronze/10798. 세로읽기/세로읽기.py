#방법 1
x = [[0] * 15 for i in range(5)]

for i in range(5):
    y = list(input())
    for j in range(len(y)):
        x[i][j] = y[j]

for i in range(15):
    for j in range(5):
        if x[j][i] == 0:
            continue;
        else:
            print(x[j][i], end='')

#방법 2
#a = []
#b = []

#for i in range(5):
#	x = input()
#	a.append(x)
#	b.append(len(x))

#t = ''

#for i in range(max(b)):
#	for j in range(5):
#		if i < b[j]:
#			t += x[j][i]

#print(t)