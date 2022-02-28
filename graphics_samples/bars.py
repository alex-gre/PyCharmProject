#!/usr/bin/env python3
# vim: set ai et ts=4 sw=4:

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv

data_names = ['cafe', 'pharmacy', 'fuel', 'bank', 'w.d.', 'atm',
              'bench', 'parking', 'restaurant', 'p.o.w.']
data_values = [9124, 8652, 7592, 7515, 7041, 6487, 6374, 6277,
               5092, 3629]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 9})

plt.title('OpenStreetMap Point Types')

ax = plt.axes()
ax.xaxis.grid(True, zorder = 1)

xs = range(len(data_names))

plt.barh([x + 0.3 for x in xs], [ d * 0.9 for d in data_values],
         height = 0.2, color = 'red', alpha = 0.7, label = '2016',
         zorder = 2)
plt.barh([x + 0.05 for x in xs], data_values,
         height = 0.2, color = 'blue', alpha = 0.7, label = '2017',
         zorder = 2)
plt.yticks(xs, data_names, rotation = 10)

plt.legend(loc='upper right')
fig.savefig('bar.png')



#Горизонтальная столбчатая диаграмма в Matplotlib
# распределение кафе по различным городам России:
#!/usr/bin/env python3
# vim: set ai et ts=4 sw=4:

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv

data_names = ['Москва', 'Санкт-Петербург', 'Сочи', 'Архангельск',
              'Владимир', 'Краснодар', 'Курск', 'Воронеж',
              'Ставрополь', 'Мурманск']
data_values = [1076, 979, 222, 189, 137, 134, 124, 124, 91, 79]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 9})

plt.title('Распределение кафе по городам России (%)')

xs = range(len(data_names))

plt.pie(
    data_values, autopct='%.1f', radius = 1.1,
    explode = [0.15] + [0 for _ in range(len(data_names) - 1)] )
plt.legend(
    bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
    loc = 'lower left', labels = data_names )
fig.savefig('pie.png')

