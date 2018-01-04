system1 = int(input('Podaj podstawe 1 systemu: '))
system2 = int(input('Podaj system na który chcesz przeliczyć liczbę: '))

liczba_do_przeliczenia = input('Podaj liczbę: ')


# Przeliczanie - liczby zwracane będa zajmować po tyle samo miejsc

def przelicznik_liter(liczba):
    if liczba < 10:
        return str(liczba)
    else:
        return chr(liczba+55)

def przelicznik_cyfr(liczba):        #
    if ord(liczba) > 47 and ord(liczba)<58:
        return int(liczba)
    else:
        return ord(liczba)-55

def sys2dec(liczba,system):
    liczba_dec = 0
    for i in range(len(liczba)):
        liczba_dec = liczba_dec*system + przelicznik_cyfr(liczba[i])
    return liczba_dec

def dec2sys(liczba,system):
    list = []
    while(liczba//system > 0):
        list.append(przelicznik_liter(liczba%system))
        liczba = liczba//system
    list.append(przelicznik_liter(liczba))
    list.reverse()
    print(''.join(list))

liczba_dec = sys2dec(liczba_do_przeliczenia,system1)
dec2sys(liczba_dec,system2)



