x = int(input())

for i in range(x):
	i += 1
	a,b = map(int,input().split())
	print("Case #%s: %s + %s = %s"%(i, a, b, a+b))
	#print("Case #"+str(i)+":",a,"+",b,"=",a+b)로 대체 가능