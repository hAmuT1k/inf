import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0, 10, 5)
y = np.random.uniform(0, 10, 5)

x1 = np.random.normal(x[0], 0.5, 10)  
x2 = np.random.normal(x[1], 0.5, 10)  
x3 = np.random.normal(x[2], 0.5, 10) 
x4 = np.random.normal(x[3], 0.5, 10) 
x5 = np.random.normal(x[4], 0.5, 10)

y1 = np.random.normal(y[0], 0.5, 10)
y2 = np.random.normal(y[1], 0.5, 10)
y3 = np.random.normal(y[2], 0.5, 10)
y4 = np.random.normal(y[3], 0.5, 10)
y5 = np.random.normal(y[4], 0.5, 10)

srx1, sry1 = np.mean(x1), np.mean(y1)
srx2, sry2 = np.mean(x2), np.mean(y2)
srx3, sry3 = np.mean(x3), np.mean(y3)
srx4, sry4 = np.mean(x4), np.mean(y4)
srx5, sry5 = np.mean(x5), np.mean(y5)

plt.scatter(x1, y1, c='red')
plt.scatter(x2, y2, c='blue')
plt.scatter(x3, y3, c='green')
plt.scatter(x4, y4, c='purple')
plt.scatter(x5, y5, c='orange')

plt.scatter(srx1, sry1, c='gray', s=150, marker='*')
plt.scatter(srx2, sry2, c='gray', s=150, marker='*')
plt.scatter(srx3, sry3, c='gray', s=150, marker='*')
plt.scatter(srx4, sry4, c='gray', s=150, marker='*')
plt.scatter(srx5, sry5, c='gray', s=150, marker='*')

plt.scatter(x[0], y[0], c='black', marker='x')
plt.scatter(x[1], y[1], c='black', marker='x')
plt.scatter(x[2], y[2], c='black', marker='x')
plt.scatter(x[3], y[3], c='black', marker='x')
plt.scatter(x[4], y[4], c='black', marker='x')

plt.legend()
plt.show()
