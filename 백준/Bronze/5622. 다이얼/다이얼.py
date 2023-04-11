s = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
x = input()
y = 0
for i in range(len(x)):
    for j in s:
        if x[i] in j:
            y += s.index(j)+3
print(y)