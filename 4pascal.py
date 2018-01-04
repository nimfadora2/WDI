
def pascal(lvl,place):
    if lvl == 0 or lvl == 1:
        return 1
    if place == 0:
        return 0
    if place == 1 or place == lvl + 1:
        return 1
    return pascal(lvl-1,place) + pascal(lvl-1,place-1)

def pascal_main(lvl):
    for i in range(lvl):
        print((lvl-1 - i) * ' ', end='')
        for j in range(i+1):
            print(pascal(i,j+1), end=" ")
        print()
    return ""


lvl = int(input("Podaj liczbę poziomów: "))
print(pascal_main(lvl))
