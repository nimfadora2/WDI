import time

def fibonacci(n):
    if n == 1:
        return 1
    if n== 0:
        return 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_iter(n):
    if n == 0: return 0
    if n==1: return 1
    n1 = 0
    n2 = 1
    for i in range(2,n+1):
        temp = n2
        n2 = n1 + n2
        n1 = temp
    return n2

liczba = int(input("Podaj liczbę poziomów: "))
prev= time.time()
print(fibonacci(liczba))
print("Czas rekurencyjnego to", prev - time.time())

prev= time.time()
print(fibonacci_iter(liczba))
print("Czas iteracyjnego to", prev - time.time())