import numpy as np
import matplotlib.pyplot as plt

def y(n):
  if n == 0:
    return 3*(-1/8)**n
  else:
    return 3*(-1/8)**n-3*(1/8)**(n-1) -(9/10)*y(n-1)

y_1 = np.zeros(10)
x = np.arange(0,10,1)
for i in x:
  y_1[i] = y(x[i])



plt.plot(x, y_1, '.')
plt.legend()
plt.grid()
plt.show()

