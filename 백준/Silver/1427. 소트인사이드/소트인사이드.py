x = list(map(int, str(input())))
x.sort(reverse=True)
for i in x:
    print(i,end='')