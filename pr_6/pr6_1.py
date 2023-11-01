n=int(input('Введите длинну массива '))
a=[]
for i in range(n):
    print('Введите',i,'элемент ')
    a.append(int(input()))
max=max(a)
print('наибольший',max)
a.reverse()
print(a)
