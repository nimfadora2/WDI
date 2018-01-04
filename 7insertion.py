from random import randint

tab = []
for i in range(0,10):
    tab.append(randint(0,10))

print("Przed posortowaniem: ",tab)
'''
for i in range(0,len(tab)):
    for j in range(i+1,len(tab)):
        if j==i+1:
            min_val=tab[j]
            min_place = j
        elif tab[j]<min_val:
            min_val=tab[j]
            min_place = j

    tab.pop(min_place)


    for k in range(0,i+1):
        if k==len(tab):
            tab.insert(k,min_val)
            break
        elif min_val < tab[k]:
            place = k
            tab.insert(k,min_val)
            break
        if k==i:
            tab.insert(k+1,min_val)
'''

def insertionsort(tablica):
    for i in range (1,len(tablica)):

        j = i-1
        while j >= 0:
            if tablica[j+1] < tablica[j]:
                tablica[j+1],tablica[j] = tablica[j], tablica[j+1]
            j-=1

insertionsort(tab)
print(tab)

