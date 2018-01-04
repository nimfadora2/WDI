import re

def podstawieniowy(teskt, alfabet):
    rezultat = []
    for letter in tekst:
        rezultat.append(alfabet[ord(letter)-97])
    return ''.join(rezultat)

def dePodstawieniowy(kod,alfabet):
    rezultat = []
    for letter in kod:
        rezultat.append(chr(alfabet.find(letter)+97))
    return ''.join(rezultat)

tekst = 'abba'

tekst = tekst.lower()
tekst = re.sub("\d","",tekst)

alfabet = 'ba'

encrypted = podstawieniowy(tekst,alfabet)
print("Zaszyfrowany teskt: ", encrypted)

decrypted = dePodstawieniowy(encrypted,alfabet)
print("Odszyfrowany tekst: ", decrypted)



