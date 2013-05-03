# -*- coding: Latin-1 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a*x**2+b*x+c
    
x = np.linspace(0, 4, 50)
#y = func(x, 3, 1.3, .5)
y = 3*np.exp(-x)*np.cos(x)+5
yn = y+0.2*np.random.normal(size=len(x))
popt, pcov = curve_fit(func, x, y)
print popt
yf = func(x, popt[0], popt[1], popt[2])
plt.plot(x,y,'+',x, yf, '-')
plt.show()