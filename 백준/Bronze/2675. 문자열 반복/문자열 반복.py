x = int(input())
for i in range(x):
    a, b = input().split()
    y = ''
    for i in b:
        y += int(a) * i
    print(y)