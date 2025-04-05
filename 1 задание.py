import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10)

plt.plot(x, x, 'r', label='y=x')          
plt.plot(x, 2*x, 'b', label='y=2x')     
plt.plot(x, 3*x, 'g', label='y=3x')     
plt.plot(x, x**2, 'y', label='y=x²')    
plt.plot(x, 2*x**2, 'gray', label='y=2x²')  

plt.title('Графики функций')      
plt.legend()                     

plt.show()                       