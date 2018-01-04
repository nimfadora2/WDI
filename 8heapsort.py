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

    print(tablica)

    for i in range (0,len(tablica)):
        print(i)
        print(tablica)
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






tablica = [1,3,4,7,5,6]
tablica = [7, 5, 9, 6, 7, 8, 10,1,2,3,4]
heapsort(tablica)