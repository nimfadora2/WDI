def mergesort(tablica):
    if len(tablica)==1:
        return tablica

    list1 = tablica[0:len(tablica)//2]
    list2 = tablica[len(tablica)//2:len(tablica)]

    list1 = mergesort(list1)
    list2 = mergesort(list2)


    return merge(list1,list2)


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


print(mergesort([1,7,5,6,2,1,3,9,0]))
