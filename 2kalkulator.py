pierwsza = int(input('Podaj pierwszą liczbę:'))
druga = int(input('Podaj drugą liczbę:'))
dzialanie = input('Podaj działanie:')

if (dzialanie=='+'):
    print(pierwsza, '+', druga, '=', pierwsza+druga)
elif (dzialanie =='-'):
    print(pierwsza, '-', druga,'=', pierwsza-druga)
elif dzialanie=='*':
    print(pierwsza, '*', druga, '=', pierwsza * druga)
elif dzialanie=='/':
    print(pierwsza, '/', druga, '=', pierwsza / druga)
else :
    print(pierwsza, '^', druga, '=', pierwsza ** druga)
