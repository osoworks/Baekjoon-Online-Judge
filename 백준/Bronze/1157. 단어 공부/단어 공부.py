x = input().upper()
y = list(set(x))
z = []

for i in y:
	z.append(x.count(i))

if z.count(max(z)) > 1:
	print("?")
else:
	print(y[(z.index(max(z)))])