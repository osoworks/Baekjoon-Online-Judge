#방법 1
#t = sorted(list(map(int, input().split())))

#print(t[0] + t[1] + min(t[2], t[0]+t[1]-1)

#방법 2
#t = sorted(list(map(int, input().split())))

#if t[0] + t[1] > t[2]:
#    print(sum(t))
#else:
#    print((t[0] + t[1]) * 2 - 1)

#방법 3
a, b, c = map(int, input().split())

x = max(a, b, c)
y = sum((a, b, c)) - x

while x >= y:
    x -= 1
print(x + y)