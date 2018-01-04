
x,y = input("Podaj x i y: ").split()

x = int(x)
y = int(y)

if x>0:
    if y>0:
        print('1')
    elif y<0:
        print('3')
    else:
        print('OY')
elif x<0:
    if y>0:
        print('2')
    elif y<0:
        print('4')
    else:
        print('OY')
else:
    if y != 0:
        print("OX")
    else:
        print("Middle")
