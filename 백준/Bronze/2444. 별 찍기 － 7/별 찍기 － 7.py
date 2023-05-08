#방법 1
#n = int(input())

#for i in range(1, n):
#    print(' '*(n-i) + '*'*(2*i-1))
#for i in range(n, 0, -1):
#    print(' '*(n-i) + '*'*(2*i-1))

#방법 2: 전체 개수 x에서 오른쪽으로 정렬하는 .center(n) 실행
x = int(input())
y = []

for i in range(1, x*2, 2):
    star = '*' * i
    y.append(star) # 별 추가

for i in range(len(y)):
    print(' ' * (x-i-1) + y[i])

y.reverse()

for i in range(1, len(y)):
    print(' ' * i + y[i])