#방법 1
#x = [1,1,2,2,2,8]
#a = list(map(int, input().split()))

#for i in range(6):
#	print(a[i] - a[i], end='')

#방법 2
a,b,c,d,e,f = map(int,input().split())
print("{} {} {} {} {} {}".format(1-a,1-b,2-c,2-d,2-e,8-f))