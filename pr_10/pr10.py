from random import randint

n = int(input())
m = int(input())
a = []
for i in range(n):
    b = []
    for j in range(m):
        b.append(randint(10, 100))
    a.append(b)

fi = open(r'C:\Users\Никита\Desktop\nikitachizhov_UB-31_vvod.txt', 'w')
for i in a:
    for j in i:
        fi.write(str(j))
        fi.write(' ')
    fi.write('\n')
fi.close()
fi = open(r'C:\Users\Никита\Desktop\nikitachizhov_UB-31_vvod.txt', 'r')

l = []
for i in fi:
    n = []
    s = i.split(' ')
    for j in s:
        if j == '\n':
            continue
        n.append(int(j))
    l.append(n)
print(l)
fi.close()

for i in l:
    mn = i.index(min(i))
    mx = i.index(max(i))
    i[mx], i[0] = i[0], i[mx]
    i[mn], i[-1] = i[-1], i[mn]

f2 = open(r'C:\Users\Никита\Desktop\nikitachizhov_UB-31_vivod.txt', 'w')
for i in l:
    for j in i:
        f2.write(str(j))
        f2.write(' ')
    f2.write('\n')
f2.close()
