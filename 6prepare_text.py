import re

tekst = 'bla5dddrfERfdvfdbRTGvcv'

nowy  = str.lower((tekst))
nowy2 = re.sub("\d+","",nowy)

print(nowy2)