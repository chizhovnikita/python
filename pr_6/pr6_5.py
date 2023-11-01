a=[]
n=int(input('введите длинну массива '))
s=0
for i in range(n):
    print('введите', i, 'элемент')
    a.append(int(input()))
for i in range(n):
    if i%2==1:
        s+=a[i]
print(s)
print(a)

