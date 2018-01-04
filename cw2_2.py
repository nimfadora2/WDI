ceny = [1,5,8,10,12,17,17,20,24,30]


whole = 17

cut = [0 for x in range(whole+1)]

max = 0

for i in range(whole+1):
    for j in range(10):
        if ((j+1) <= i):                    #czy zmiesci sie w plecaku o rozmoaezie i
           cut[i]=cut[i] if cut[i] > cut[i-j-1]+ceny[j] else cut[i-j-1]+ceny[j]

print(cut[17])



