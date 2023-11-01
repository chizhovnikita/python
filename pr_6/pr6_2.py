n=int(input('введите длинну массива: '))
a=[]
for i in range(n):
    print('введите',i,'элемент')
    a.append(int(input()))
s=sum(a)
sr=s/len(a)
for i in range(len(a)):
    if a[i]==0:
        a[i]=sr
print(a)