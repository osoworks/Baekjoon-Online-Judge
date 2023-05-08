n, m = map(int, input().split())
x = [t+1 for t in range(n)]

for _ in range(m):
  i, j, k = map(int, input().split())
  x = x[:i-1] + x[k-1:j] + x[i-1:k-1] + x[j:]

for b in x:
  print(b, end=' ')