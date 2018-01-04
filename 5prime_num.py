

#lista = [int(x) for x in input('Podaj wektor liczb:').split()]

lista2 = [2,3,3,4,5,3]

lista2.sort()
max = lista2[len(lista2)-1]

print(max)

# Liczby pierwsze
numbers = list(range(1, max + 1))
for x in numbers:
    if x != 1:
        lista = list(range((x + x), (max + 1), x))
        numbers = [x for x in numbers if x not in lista]



for i in lista2:
    repeat = [x for x in lista2 if x in numbers and x==i]
    print(repeat)
    if len(repeat) > 0 and len(repeat)%2 == 1:
        lista2 = [x for x in lista2 if x not in repeat]
    print("lista: ", lista2)

print(lista2)
