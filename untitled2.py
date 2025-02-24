# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-rx7-p1meo5VVt-WIkZyibjpsFAU-dDK
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2, 8, 12, 20])
y = np.array([1, 7, 3, 5])

plt.plot(x, y)
plt.show()

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([0, 0.2, 0, -0.8, 0, 1.8, 0, -0.3, 0, 0.5, 0])

plt.plot(x, y)
plt.show()

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([2, 9, 18, 36, 81, 162, 324])

plt.scatter(x, y)
plt.show()

y = np.array([4, 12, 3, 10])

plt.plot(y, 'o--b')
plt.show()

y = np.array([4, 7, 6, 9])

plt.pie(y)
plt.show()

y = np.array([4, 8, 6, 10])
x = np.array([9, 3, 5, 4])
y2 = np.array([2, 10, 6, 9])
x2 = np.array([3, 10, 5, 8])

plt.plot(y, x, y2, x2)
plt.show()

x = np.array([5, 9, 12, 18])
y = np.array([10, 15, 20, 25])

plt.scatter(x, y, color='yellow')

x = np.array([4, 6, 14, 30])
y = np.array([30, 10, 20, 40])

plt.scatter(x, y, color='blue')

plt.show()

x = np.array(['W', 'X', 'Y', 'Z'])
y = np.array([3, 7, 4, 6])

plt.bar(x, y)
plt.show()

x = np.array(['W', 'X', 'Y', 'Z'])
y = np.array([3, 7, 4, 6])

plt.barh(x, y)
plt.show()

y = np.array([5, 8, 4, 6])
mylabels = ['alpha', 'beta', 'gamma', 'delta']

plt.pie(y, labels=mylabels)
plt.show()

y = np.array([5, 8, 4, 6])
mylabels = ['alpha', 'beta', 'gamma', 'delta']
myexplode = [0.3, 0, 0, 0]

plt.pie(y, labels=mylabels, explode=myexplode)
plt.show()

y = np.array([5, 8, 4, 6])
mylabels = ['alpha', 'beta', 'gamma', 'delta']
myexplode = [0.3, 0, 0, 0]

plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
plt.show()

y = np.array([5, 8, 4, 6])
mylabels = ['alpha', 'beta', 'gamma', 'delta']
myexplode = [0.3, 0, 0, 0]

plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
plt.legend(title='Labels:')
plt.show()