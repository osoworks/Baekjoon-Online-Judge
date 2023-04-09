#방법 1
x = int(input())
y = ''

for i in range(1,int(x//4)+1):
	if i != (x//4):
		y += "long "
	else:
		y += "long int"
print(y)

#방법 2
#x = int(input())
#y = 'int'
#for i in range(x//4):
#    y = 'long ' + y
#print(y)

#방법 3
#print(int(input())//4 * "long " + "int")

#방법 4
#for i in range(int(input()) // 4):
#    print("long", end="")  
#print("int")