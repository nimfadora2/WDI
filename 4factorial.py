import time

def silnia(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    return n*silnia(n-1)

def silnia_iter(n):
    if n == 0: return 1
    wynik = 1
    for i in range(n):
        wynik = wynik*(i+1)
    return wynik

liczba = int(input("Podaj liczbę dla której jest liczona silnia: "))
prev= time.time()
print(silnia(liczba))
print("Czas rekurencyjnego to", prev - time.time())

prev= time.time()
print(silnia_iter(liczba))
print("Czas iteracyjnego to", prev - time.time())
