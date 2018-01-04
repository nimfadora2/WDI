from time import time

dane = [10, 100, 500,1000,4000, 5500, 7000, 10000, 13000, 15000, 20000, 25000]
timey=[]
for max in dane:
    numbers = list(range(1,max+1))
    prev = time()
    for x in numbers:
        if x != 1:
            lista = list(range((x+x),(max+1),x))
            numbers = [x for x in numbers if x not in lista]
    time_l=time()-prev
    timey.append(time_l)

print(timey)
'''
Source:
https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html
https://stackoverflow.com/questions/35166633/how-do-i-multiply-each-element-in-a-list-by-a-number
'''

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(dane,[i*1000 for i in timey], '.-')
ax.set(xlabel='Max', ylabel='Czas [ms]', title='Czas działania programu w zależności od max')

ax.grid()

fig.savefig("test.png")
plt.show()

