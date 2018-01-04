import random

tablica = []
for i in range(50):
    tablica.append(random.randint(0,100))

# Quicksort
def quicksort(tablica,poczatek,koniec):
    if koniec - poczatek > 0:
        p = divide(tablica,poczatek,koniec)
        quicksort(tablica,poczatek,p-1)
        quicksort(tablica,p+1,koniec)
# Divide dto quicksort
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

# Merge sort
def mergesort(tablica):
    if len(tablica)==1:
        return tablica

    list1 = tablica[0:len(tablica)//2]
    list2 = tablica[len(tablica)//2:len(tablica)]

    list1 = mergesort(list1)
    list2 = mergesort(list2)

    return merge(list1,list2)
# Merge for merge sort
def merge(list1,list2):
    list_end = []
    i,j=0,0
    while i < len(list1) or j < len(list2):
        if i==len(list1):
            list_end.append(list2[j])
            j+=1
        elif j==len(list2):
            list_end.append(list1[i])
            i+=1
        elif list1[i] < list2[j]:
            list_end.append(list1[i])
            i+=1
        elif list1[i] > list2[j]:
            list_end.append(list2[j])
            j+=1
        else:
            list_end.append(list2[j])
            list_end.append(list2[j])
            j+=1
            i+=1
    return list_end

# Heap sort
def heapsort(tablica):

    if len(tablica) == 1 or len(tablica)==0:
        return tablica

    #create heap
    for i in range (1,len(tablica)):
        parent = (i-1)//2
        child = i
        while parent >= 0 and tablica[parent] < tablica[child]:
            tablica[parent],tablica[child] = tablica[child],tablica[parent]
            child = parent
            parent = (parent-1)//2
    if len(tablica)==2:
        return tablica
    # sort
    for i in range (0,len(tablica)):
        tablica[0],tablica[len(tablica)-i-1]= tablica[len(tablica)-i-1],tablica[0]

        parent = 0
        child1 = 1
        child2 = 2
        if child1 >=len(tablica)-i-1:
            child1=parent
        if child2 >= len(tablica)-i-1:
            child2=child1


        while (tablica[parent] < tablica[child1] or tablica[parent] < tablica[child2]):
            if tablica[child2] > tablica[child1]:
                tablica[child2], tablica[parent] = tablica[parent],tablica[child2]
                parent = child2
            else:
                tablica[child1], tablica[parent] = tablica[parent], tablica[child1]
                parent = child1

            if 2*parent+1 > len(tablica)-i-2:
                child1 = parent
                child2 = parent
            elif  2*parent+2 > len(tablica)-i-2:
                child1 = 2*parent+1
                child2 = child1
            else:
                child1 = 2*parent + 1
                child2 = 2*parent + 2

# Bubble sort
def bubblesort(tablica):
    flag = True
    k=0
    while(flag==True):
        flag = False
        for j in range(0,len(tablica)-1-k):
            if tablica[j+1]<tablica[j]:
                flag = True
                tablica[j+1],tablica[j]=tablica[j],tablica[j+1]
        k+=1

# Selection sort
def selectionsort(tablica):
    for i in range(0,len(tablica)):
        for j in range(i,len(tablica)):
            if j==i:
                min_val = tablica[j]
                min_place = j
            else:
                if tablica[j]<min_val:
                    min_val = tablica[j]
                    min_place = j
        tablica[i],tablica[min_place]=tablica[min_place],tablica[i]

# Insertionsort
def insertionsort(tablica):
    for i in range (1,len(tablica)):

        j = i-1
        while j >= 0:
            if tablica[j+1] < tablica[j]:
                tablica[j+1],tablica[j] = tablica[j], tablica[j+1]
            j-=1


print(tablica)

tablica_quick = list(tablica)
quicksort(tablica_quick,0,len(tablica)-1)
print(tablica_quick)

tablica_merge = list(tablica)
tablica_merge=mergesort(tablica_merge)
print(tablica_merge)

tablica_heap = list(tablica)
heapsort(tablica_heap)
print(tablica_heap)

tablica_bubble = list(tablica)
bubblesort(tablica_bubble)
print(tablica_bubble)

tablica_select = list(tablica)
selectionsort(tablica_select)
print(tablica_select)

tablica_insert = list(tablica)
insertionsort(tablica_insert)
print(tablica_insert)