"""
Simple demo of a scatter plot.
"""
import numpy as np
import matplotlib.pyplot as plt


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
x1 = np.random.rand(N+10)
y1 = np.random.rand(N+10)
x1 = np.random.rand(N+20)
y1 = np.random.rand(N+20)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses
	
plt.scatter([1, 2, 3, 4], [5, 4, 3, 2], s=area, c='red', alpha=0.2)
plt.scatter(x1, y1, s=area, c=colors, alpha=1)

plt.show()
