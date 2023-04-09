x = int(input())
for i in range(x):
	i += 1
	a,b = map(int,input().split())
	print("Case #%s: %s"%(i, a+b))
	#print("Case #"+str(i)+":",a+b)로도 대체 가능