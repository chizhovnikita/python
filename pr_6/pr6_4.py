n=int(input('введите длинну массива: '))
a=[]
pol=[]
otr=[]
for i in range(n):
    print('введите',i,'элемент')
    a.append(int(input()))
for i in a:
    if i>0:
        pol.append(i)
    else:
        otr.append(i)
print(pol)
print(otr)
