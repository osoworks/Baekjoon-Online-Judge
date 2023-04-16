x = []

for i in range(10) :   
    y = int(input())
    x.append(y % 42) 

print(len(set(x)))