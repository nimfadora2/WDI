def quicksort(tablica,poczatek,koniec):
    if koniec - poczatek > 0:
        p = divide(tablica,poczatek,koniec)
        quicksort(tablica,poczatek,p-1)
        quicksort(tablica,p+1,koniec)


def divide(tablica,poczatek,koniec):

    index = koniec
    value = tablica[index]
    #print(value)
    left = poczatek
    right = koniec-1
    done = False

    while not done:
        #print(tablica[left], tablica[right], left, right)
        if left >= right:
            if left == koniec:
                return left
            if value < tablica[left]:
                tablica[left],tablica[koniec] = tablica[koniec],tablica[left]
                return left
            else:
                left+=1
        elif tablica[left] < value:
            left+=1
        elif tablica[right] > value:
            right-=1
        else:
            tablica[left],tablica[right]=tablica[right],tablica[left]
            left+=1
            right-=1
        #print(tablica)





tablica = [0,6,1,2,3,4,5,7,2,9]
print(tablica)
quicksort(tablica,0,len(tablica)-1)
print(tablica)