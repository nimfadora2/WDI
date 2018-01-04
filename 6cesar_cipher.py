import re
import string

def przesun(letter,number):
    place = ord(letter)
    new_place = place+number
    if new_place < 97:
        new_place +=26
    elif new_place > 122:
        new_place -=26
    return chr(new_place)


def cezar(tekst,przesuniecie):
    table =[]
    for letter in tekst:
        table.append(przesun(letter,przesuniecie))
    return table

def decezar(tekst,przesuniecie):
    return cezar(tekst,-przesuniecie)



tekst = 'kinga'

tekst = tekst.lower()
tekst = re.sub("\d","",tekst)

nr_places = 2

encrypted = ''.join(cezar(tekst, nr_places))

print('Zaszyfrowany tekst: ', encrypted)

decrypted = ''.join(decezar(encrypted,nr_places))
print('Odzyfrowany tekst: ', decrypted)