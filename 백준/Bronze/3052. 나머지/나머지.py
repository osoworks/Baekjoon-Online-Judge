lst = []

for _ in range(10) :   
    num = int(input())
    lst.append(num%42) 

print(len(set(lst)))
