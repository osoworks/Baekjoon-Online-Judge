#방법 1
a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a*i) + (b*j) == c and (d*i) + (e*j) == f:
            print(i,j)
            
#방법 2
#a, b, c, d, e, f = map(int, input().split())
#print((c*e-b*f)//(a*e-b*d), (a*f-d*c)//(a*e-b*d))