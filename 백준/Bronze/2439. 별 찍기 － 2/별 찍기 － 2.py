#방법 1: 1 ~ n 기준으로 진행
x = int(input())
for i in range(1, x+1):
	print(" " * (x-i) + "*" * i)

#방법 2: 0 ~ n-1 기준으로 진행
#x = int(input())
#for i in range(x):
#	print(" " * (x-i-1) + "*" * (i+1))

#방법 3: 전체 개수 x에서 오른쪽으로 정렬하는 .rjust(n) 실행
#x = int(input())
#for i in range(x):
#	star = "*" * (i+1)
#	print(star.rjust(n))