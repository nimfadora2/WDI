from random import randint

tab = []
for i in range(0,10):
    tab.append(randint(0,10))

print(tab)


def bubblesort(tablica):
    flag = True
    k=0
    while(flag==True):
        flag = False
        for j in range(0,len(tab)-1-k):
            if tab[j+1]<tab[j]:
                flag = True
                tab[j+1],tab[j]=tab[j],tab[j+1]
        k+=1

bubblesort(tab)
print(tab)
