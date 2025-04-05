import matplotlib.pyplot as plt
import numpy as np

sub = ['Аэронавигация', 'Высшая математика', 'Метеорология', 'ОТП']
grad = [
    [5, 5, 5, 5],  # Аэронавигация
    [5, 4, 5, 4],  # Высшая математика
    [5, 4, 3, 4],  # Метеорология
    [4, 4, 4, 4]   # ОТП
]

dat = ['09.09', '09.10', '09.11', '09.12']

bar_width = 0.2
x1 = np.arange(len(dat))
x2 = [x + bar_width for x in x1]
x3 = [x + bar_width for x in x2]
x4 = [x + bar_width for x in x3]

plt.bar(x1, grad[0], width=bar_width, label=sub[0], color='blue')
plt.bar(x2, grad[1], width=bar_width, label=sub[1], color='red')
plt.bar(x3, grad[2], width=bar_width, label=sub[2], color='green')
plt.bar(x4, grad[3], width=bar_width, label=sub[3], color='purple')

plt.xlabel('Дата')
plt.ylabel('Оценка')
plt.xticks([x + bar_width*1.5 for x in range(len(dat))], dat)


plt.ylim(2, 5.5)

plt.legend()

plt.show()
