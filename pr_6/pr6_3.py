n=int(input('введите длинну массива: '))
a=[]
for i in range(n):
    print('введите',i,'элемент')
    a.append(int(input()))
min=min(a)
m=a.index(min)
print(m)
