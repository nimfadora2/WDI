from random import randint

tab = []
for i in range(0,10):
    tab.append(randint(0,10))

print("Przed posortowaniem: ",tab)


for i in range(0,len(tab)):
    for j in range(i,len(tab)):
        if j==i:
            min_val = tab[j]
            min_place = j
        else:
            if tab[j]<min_val:
                min_val = tab[j]
                min_place = j
    tab[i],tab[min_place]=tab[min_place],tab[i]

print("Po posortowaniu: ", tab)


