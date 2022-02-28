import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#программа колхоз
#программа показатели сбора урожая за неделю

#записи в матрицу вида 5Х4 (5 дней)X(4 бригады)

#бригада blue
values1 = [int(input("Бригада Blue ["+str(i)+"]="))
for i in range(0,5)]
print('\n')

#бригада green
values2 = [int(input("Бригада Green ["+str(i)+"]="))
for i in range(0,5)]
print('\n')

#бригада red
values3 = [int(input("Бригада Red ["+str(i)+"]="))
for i in range(0,5)]
print('\n')

#бригада red
values4 = [int(input("Бригада Yellow ["+str(i)+"]="))
for i in range(0,5)]
print('\n')

index = np.arange(5)

#ширина столбцов графика
bw = 0.12

#axis() уст. значения по горизонту и вертикали
plt.axis([0,5,0,8])
#шапка графика
plt.title('Колхозное соревнование', fontsize=20)
#задается ширина и цвет столбцов 
plt.bar(index, values1, bw, color='b')
plt.bar(index+bw, values2, bw, color='g')
plt.bar(index+2*bw, values3, bw, color='r')
plt.bar(index+3*bw, values4, bw, color='y')
plt.xticks(index+1.5*bw,['пн','вт','ср','чт','пт'])
plt.show()
