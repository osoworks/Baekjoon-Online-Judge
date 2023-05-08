n = int(input())
m = list(map(int, input().split()))
c = 0

for x in m:
  for i in range(2, x+1):
    if x % i == 0:
      if x == i:
        c += 1
      break
print(c)