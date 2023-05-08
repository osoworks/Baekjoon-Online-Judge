x = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
y = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

a = 0	#학점 총합
b = 0	#(학점 * 과목평점) 총합

for _ in range(20) :
	s, p, g = input().split()
	p = float(p)
	
	if g != 'P' :	#등급이 P인 과목은 포함X
		a += p
		b += p * y[x.index(g)]

print('%.6f' % (b / a))