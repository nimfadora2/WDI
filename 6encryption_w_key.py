import re

def zKluczem(teskt, klucz):
    rezultat = []
    for i in range(len(tekst)):
        new_place = ord(tekst[i]) + (ord(klucz[i]) - 96)
        if new_place < 97:
            new_place += 26
        elif new_place > 122:
            new_place -= 26
        rezultat.append(chr(new_place))
    return ''.join(rezultat)

def deZKluczem(kod, klucz):
    rezultat = []
    for i in range(len(kod)):
        new_place = ord(kod[i]) - (ord(klucz[i]) - 96)
        if new_place < 97:
            new_place += 26
        elif new_place > 122:
            new_place -= 26
        rezultat.append(chr(new_place))
    return ''.join(rezultat)


tekst = 'abba'

tekst = tekst.lower()
tekst = re.sub("\d","",tekst)

klucz = 'baba'

encrypted = zKluczem(tekst,klucz)
print(zKluczem(tekst,klucz))

decrypted = deZKluczem(encrypted,klucz)
print(decrypted)
