#방법 1
x = input()
y = list(range(97,123)) #아스키코드 숫자 범위

for i in y:
    print(x.find(chr(i)))

#방법 2
#x = input()
#y ='abcdefghijklmnopqrstuvwxyz'
#for i in y:
#    if i in x:
#        print(x.index(i), end= ' ')
#    else:
#        print(-1, end =' ')