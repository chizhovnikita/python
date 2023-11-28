a=input('фигура: ')
def круг():
    r= int(input('Введите радиус: '))
    p=3.14
    s=p*(r**2)
    print(s)
def квадрат():
    a=int(input('Введите сторону: '))
    s=a**2
    print(s)
def треугольник():
    a=int(input('Введите сторону: '))
    h=int(input('Введите высоту: '))
    s=0.5*a*h
    print(s)
if a == 'круг':
    print(круг())
elif a == 'квадрат':
    print(квадрат())
elif a == 'треугольник':
    print(треугольник())
