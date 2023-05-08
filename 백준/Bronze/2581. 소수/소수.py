m = int(input())
n = int(input())
x = []

for i in range(m,n+1):
    c = 0
    if i > 1:
        for j in range(2,i):
            if i % j==0:
                c += 1
                break
        if c == 0:
            x.append(i)

if len(x) < 1:
    print(-1)
else:
    print(sum(x))
    print(min(x))