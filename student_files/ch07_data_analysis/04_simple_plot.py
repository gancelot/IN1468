import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11)
y = 10 * np.random.rand(10)
plt.ylabel('Random Values')
plt.xlabel('Numbers')
plt.plot(x, y, 'ro')

x2 = np.arange(2, 11, 2)
y2 = 10 * np.random.rand(5)
plt.plot(x2, y2)

plt.show()
