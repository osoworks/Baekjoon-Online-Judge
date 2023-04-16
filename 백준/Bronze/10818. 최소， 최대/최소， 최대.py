x = int(input())
y = list(map(int, input().split()))

z = sorted(y)
print(z[0], z[-1])